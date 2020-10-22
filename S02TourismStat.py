#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *
import param
import luigi


def extract_tourism_stat(inputfilename, year):
    csv_header = [
        "area",
        "promotion_bureau",
        "commune",
        "type",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
        "january",
        "february",
        "march",
        "sum",
        "previous_year",
        "comparison_with_previous_year",
    ]
    records = []
    with open(inputfilename) as f:
        last_area = ""
        last_promotion_bureau = ""
        last_commune = ""
        reader = csv.reader(f)
        for row in reader:
            # 飛ばす条件
            if (
                len(row) == 0
                or row[0] == "圏　域"
                or row[0] == "　圏　域"
                or len(row) == 1
                or row[6] == ""
            ):
                continue
            # 補完代入
            if row[0] != "":
                area = row[0].replace("圏域", "").replace("計", "").replace("　", "")
                if area == "オホーツ":
                    area = "オホーツク"
                if area == "釧路・根":
                    area = "釧路・根室"
                if len(area) > 0 and len(area) != 3 and last_area != area:
                    last_area = area
                    last_promotion_bureau = ""
                    last_commune = ""
                    continue
            if row[1] != "":
                promotion_bureau = (
                    row[1]
                    .replace("支庁計", "")
                    .replace("支庁", "")
                    .replace("総合振興局計", "")
                    .replace("振興局計", "")
                    .replace("　", "")
                )
                if last_promotion_bureau != promotion_bureau:
                    last_promotion_bureau = promotion_bureau
                    last_commune = ""
                    continue
            if row[2] != "":
                row[2] = row[2].replace("中礼内", "中札内").replace("（定山渓を除く）", "")
                last_commune = row[2]
            # skip
            if last_commune == "" or last_commune == "":
                continue
            row[0] = last_area.replace("圏域計", "").replace("　", "")
            row[1] = last_promotion_bureau.replace("計", "")
            row[2] = last_commune
            if 2003 <= year <= 2009:  # and len(record)>=21):
                del row[17:18]
                del row[10:11]
            records.append(row)
    return csv_header, records


class ConvertToCSV(luigi.Task):
    target = luigi.DictParameter()

    def requires(self):
        return downloader(filepath=self.target["filename"], url=self.target["url"])

    def output(self):
        target = self.target
        filename_csv = "var/raw_{}_{}_monthly.csv".format(
            target["name"], target["year"]
        )
        return luigi.LocalTarget(filename_csv, format=luigi.format.UTF8)

    def run(self):
        target = self.target
        with self.output().open("w") as outfile:
            excel2csv(
                infile=target["filename"],
                outfile=outfile,
                filetype=target["type"],
                sheetname=target["sheets"]["monthly"],
            )


class ExtractTourismStatTask(luigi.Task):
    target = luigi.DictParameter()
    sheet = luigi.IntParameter()

    def requires(self):
        return ConvertToCSV(self.target)

    def output(self):
        target = self.target
        i = self.sheet
        filename_extracted = "data/{}_{}_monthly.csv".format(
            target["name"], target["year"]
        )
        return luigi.LocalTarget(filename_extracted, format=luigi.format.UTF8)

    def run(self):
        target = self.target
        header, records = extract_tourism_stat(
            self.input().fn, year=int(target["year"])
        )
        with self.output().open("w") as f:
            f.write(",".join(header))
            f.write("\n")
            for record in records:
                f.write(",".join(record))
                f.write("\n")


class FetchAllTourismStatTask(luigi.WrapperTask):
    def __init__(self) -> None:
        super().__init__()
        targets = []
        for group in param.tourism_stat_report_targets:
            for target in group["targets"]:
                filename = "var/{}_{}.{}".format(
                    group["name"], target["year"], target["type"]
                )
                output = {
                    "name": group["name"],
                    "year": target["year"],
                    "filename": filename,
                    "url": target["url"],
                    "type": target["type"],
                    "sheets": target["sheets"],
                }
                targets.append(output)
        self.targets = targets

    def requires(self):
        for target in self.targets:
            for i in range(len(target["sheets"])):
                yield ExtractTourismStatTask(target=target, sheet=i)


if __name__ == "__main__":
    luigi.run(["FetchAllTourismStatTask", "--local-scheduler"])
