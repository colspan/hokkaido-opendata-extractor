# -*- coding: utf-8 -*-
import luigi

import requests


class downloader(luigi.Task):
    filepath = luigi.Parameter()
    url = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.filepath, format=luigi.format.Nop)

    def run(self):
        r = requests.get(self.url)
        with self.output().open("wb") as f:
            f.write(r.content)


# https://github.com/dilshod/xlsx2csv
# https://github.com/hempalex/xls2csv
import external.xls2csv as xls2csv
import xlsx2csv


def excel2csv(infile, outfile, filetype, sheetid=None, sheetname=None):
    if filetype == "xlsx":
        parser = xlsx2csv.Xlsx2csv(infile)
        if sheetid is None and sheetname is not None:
            sheetid = parser.getSheetIdByName(sheetname)
        parser.convert(outfile, sheetid=sheetid)
    elif filetype == "xls":
        xls2csv.xls2csv(
            infile, outfile, sheetid=sheetid, sheetname=sheetname, encoding="cp932"
        )


import csv
import re
import param


def extractCommuneStat(infilepath, outfilepath, csv_title):
    rows = []
    col_nums = []
    row_num = 0
    with open(infilepath, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            col_nums.append(len(row))
            rows.append(row)
            row_num += 1
    commune_nums = []
    first_row_nums = []
    null_nums = []
    for col in range(col_nums[0]):
        commune_count = 0
        first_row_num = -1
        null_count = 0
        for i, row in enumerate(rows):
            text = row[col].replace("　", "").replace(" ", "")
            if text == "":
                null_count += 1
            if text in param.communes:
                commune_count += 1
                if first_row_num == -1:
                    first_row_num = i
        commune_nums.append(commune_count)
        first_row_nums.append(first_row_num)
        null_nums.append(null_count)
    for i, x in enumerate(reversed([x != row_num for x in null_nums])):
        if x:
            end_col_num = len(null_nums) - i
            break
    # 市町村名カラム
    begin_col_num = commune_nums.index(max(commune_nums))
    [x != row_num for x in null_nums]
    new_rows = []
    for row in rows:
        text = row[begin_col_num] = row[begin_col_num].replace("　", "").replace(" ", "")
        if not text in param.communes:
            # 市町村名がなかったら飛ばす
            continue
        new_rows.append(
            [re.sub("^-+$", "0", x) for x in row[begin_col_num:end_col_num]]
        )
    # 外部からのカラム名の代入を受け付ける TODO
    # カラム名候補の文字列を抽出する
    col_names = {}
    re_numeric = re.compile("-*[0-9]+(\.[0-9]+)*")
    for col_i in range(begin_col_num + 1, end_col_num):
        tmp = []
        for row_i, row in enumerate(rows):
            if row_i > first_row_nums[begin_col_num]:
                break
            if row[col_i] != "" and not re_numeric.match(row[col_i]):
                output_str = re.sub(" +", "", row[col_i].replace("　", " "))
                tmp.append(output_str)
        col_names[col_i] = "{:02d}_{}".format(
            col_i, "".join(tmp).replace("北海道", "").replace("\n", "")
        )
    col_names[0] = csv_title
    # 出力
    writer = csv.writer(open(outfilepath, "w"))
    writer.writerow(col_names.values())
    for row in new_rows:
        writer.writerow(row)


class SimpleTask(luigi.WrapperTask):
    completed = False

    def complete(self):
        return self.completed

    def on_success(self):
        self.completed = True
