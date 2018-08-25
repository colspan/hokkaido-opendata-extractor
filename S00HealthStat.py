#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *
import param
import luigi

var_target_files = []
for group in param.health_stat_report_targets:
    for url in group["urls"]:
        filename = "var/{}_{}_{}.{}".format(group["name"],url["year"],group["subname"],url["type"])
        output = {
            "name":group["name"],
            "subname":group["subname"],
            "year":url["year"],
            "filename":filename,
            "url":url["url"],
            "type":url["type"],
            "sheets":group["sheets"]
        }
        var_target_files.append(output)

class ConvertToCSV(luigi.Task):
    target = luigi.DictParameter()
    sheet = luigi.IntParameter()
    def requires(self):
        return downloader(filepath=self.target["filename"],url=self.target["url"])
    def output(self):
        target = self.target
        i = self.sheet
        filename_csv = "var/{}_{}_{:02d}.csv".format(target["name"],target["year"],(int(target["subname"].split('-')[0])+i))
        filename_extracted = "var/extracted_{}_{}_{:02d}.csv".format(target["name"],target["year"],(int(target["subname"].split('-')[0])+i))
        return [luigi.LocalTarget(filename_csv), luigi.LocalTarget(filename_extracted)]       
    def run(self):
        target = self.target
        i = self.sheet
        excel2csv( infilepath=target["filename"], outfilepath=self.output()[0].fn, filetype=target["type"], sheetid=i+1 )
        extractCommuneStat(infilepath=self.output()[0].fn, outfilepath=self.output()[1].fn, csv_title=target["sheets"][i])

class D04S00mainTask(luigi.WrapperTask):
    def requires(self):
        for target in var_target_files:
            for i in range(len(target["sheets"])):
                yield ConvertToCSV(target=target, sheet=i)

if __name__ == "__main__":
    luigi.run(['D04S00mainTask', '--local-scheduler'])
