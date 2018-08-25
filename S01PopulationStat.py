#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *
import param
import luigi

classes = [
    "総数",
    "0～4歳",
    "5～9歳",
    "10～14歳",
    "15～19歳",
    "20～24歳",
    "25～29歳",
    "30～34歳",
    "35～39歳",
    "40～44歳",
    "45～49歳",
    "50～54歳",
    "55～59歳",
    "60～64歳",
    "65～69歳",
    "70～74歳",
    "75～79歳",
    "80～84歳",
    "85～89歳",
    "90～94歳",
    "95～99歳",
    "100歳以上",
]
nationalities = ["日本人", "外国人", "国籍計"]
genders = ["男", "女", "男女計"]

def extract_cols(row):
    return
def extractPopulation(infilepath, outfilepath, csv_title, year):
    df = {}
    communes = []
    rows = []
    with open(infilepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    for row in rows[5:]:
        commune_name = row[1].replace(" ","").replace("　","")
        if commune_name == "":
            continue
        else:
            communes.append(commune_name)
    for i, nationality in enumerate(nationalities):
        rows_male = []
        rows_female = []
        rows_sum = []
        for row in rows[5:]:
            extracted_cols = []
            for j in range(len(classes)):
                extracted_cols.append(row[3+len(nationalities)*j+i])
            if   row[2] == "男":
                rows_male.append(extracted_cols)
            elif row[2] == "女":
                rows_female.append(extracted_cols)
            elif row[2] == "計":
                rows_sum.append(extracted_cols)

        df[nationality] = {
            "男" : rows_male,
            "女" : rows_female,
            "男女計" : rows_sum
        }

    csv_header = ["階級別人口{}年".format(year)]
    for gender in ["男女計", "男", "女"]:
        for nationality in ["国籍計", "日本人", "外国人"]:
            for class_name in classes:
                csv_header.append("{}({})({})".format(class_name, nationality, gender))

    csv_rows = []
    for row_i in range(len(df["国籍計"]["男"])):
        csv_row = [communes[row_i]]
        for gender in ["男女計", "男", "女"]:
            for nationality in ["国籍計", "日本人", "外国人"]:
                csv_row += df[nationality][gender][row_i]
        csv_rows.append(csv_row)

    writer = csv.writer(open(outfilepath, 'w'))
    writer.writerow(csv_header)
    for row in csv_rows:
        writer.writerow(row)

class ConvertToCSV(luigi.Task):
    url = luigi.Parameter()
    year = luigi.Parameter()
    def requires(self):
        return downloader(filepath='var/population_{}.xls'.format(self.year), url=self.url)
    def output(self):
        filename_csv = 'var/population_{}.csv'.format(self.year)
        filename_extracted_csv = 'var/extracted_population_{}.csv'.format(self.year)
        return [luigi.LocalTarget(x) for x in [filename_csv, filename_extracted_csv]]
    def run(self):
        excel2csv( infilepath=self.input().fn, outfilepath=self.output()[0].fn, filetype='xls', sheetid=1 )
        extractPopulation(infilepath=self.output()[0].fn, outfilepath=self.output()[1].fn, csv_title='population {}'.format(self.year), year=self.year)

class D04S01mainTask(luigi.WrapperTask):
    def requires(self):
        for k,v in param.population_targets.items():
            yield ConvertToCSV(url=v, year=k)

if __name__ == "__main__":
    luigi.run(['D04S01mainTask', '--local-scheduler'])
