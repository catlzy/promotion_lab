import sys
import csv
import xlrd

def main(col_names):
    if len(sys.argv) < 2:
        print ("Please specify input csv file name")
        return

    csv_file_name = sys.argv[1]
    book = xlrd.open_workbook(csv_file_name)
    sheet = book.sheet_by_index(0)
    headers = sheet.row_values(0)
    processed = {}

    for h in headers:
        if h in col_names:
            col_val = sheet.col_values(headers.index(h), 1)
            processed[h] = []
            avg = sum(col_val)/len(col_val)
            num_cat = 10
            max_val = max(col_val)
            min_val = min(col_val)
            diff = max_val - min_val
            for v in col_val:
                # if v < avg/3:
                #     processed[h].append("%.4f" % (avg/3))
                # elif v < avg/3*2:
                #     processed[h].append("%.4f" % (avg/3*2))
                # elif v < avg:
                #     processed[h].append("%.4f" % (avg))
                # elif v < avg/3*4:
                #     processed[h].append("%.4f" % (avg/3*4))
                # elif v < avg/3*5:
                #     processed[h].append("%.4f" % (avg/3*5))
                # elif v < avg*2:
                #     processed[h].append("%.4f" % (avg*2))
                # else:
                #     processed[h].append("%.4f" % (max_val))
                for i in range(1, num_cat+1):
                    if v < min_val+diff/num_cat*i:
                        processed[h].append("%.4f" % (min_val+diff/num_cat*i))
                        break
                    elif i == num_cat:
                        processed[h].append("%.4f" % (min_val+diff/num_cat*i))
        elif h == 'CLUSTYPE':
            processed[h] = []
            col_val = sheet.col_values(headers.index('CLUSTYPE'), 1)
            most_common = ['1', '4', '8', '10', '15', '16']
            for v in col_val:
                if str(int(v)) not in most_common:
                    processed[h].append("other")
                else:
                    processed[h].append(str(int(v)))
        elif h != 'CUSTOMER_ID':
            processed[h] = sheet.col_values(headers.index(h), 1)


    plist = [headers[1:]]
    for i in range(len(sheet.col_values(0, 1))):
        entries = []
        for h in headers[1:]:
            entries.append(processed[h][i])
        plist.append(entries)
    with open('processed.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(plist)


if __name__ == "__main__":
    col_names = ['ZIP_CODE', 'TOTAL_VISITS', 'TOTAL_SPENT', 'AVRG_SPENT_PER_VISIT', 'PSWEATERS', 'PKNIT_TOPS', 'PKNIT_DRES', 'PBLOUSES', 'PJACKETS',
                'PCAR_PNTS', 'PCAS_PNTS', 'PSHIRTS', 'PDRESSES', 'PSUITS', 'POUTERWEAR', 'PJEWELRY', 'PFASHION', 'PLEGWEAR',
                 'PCOLLSPND', 'AMSPEND', 'PSSPEND', 'CCSPEND', 'AXSPEND', 'SPEND_LAST_MONTH', 'SPEND_LAST_3MONTH',
                 'SPEND_LAST_6MONTH', 'SPENT_LAST_YEAR', 'GMP', 'PROMOS_ON_FILE', 'DAYS_ON_FILE', 'FREQ_DAYS', 'MARKDOWN',
                 'PRODUCT_CLASSES', 'COUPONS', 'STYLES', 'STORES', 'STORELOY', 'MAILED', 'RESPONDED', 'RESPONSERATE', 'LTFREDAY', 'PERCRET']
    main(col_names)
