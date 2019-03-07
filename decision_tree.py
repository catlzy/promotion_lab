import dtree_build
import sys
import csv
from sklearn.utils import resample


def main(col_names=None):
    if len(sys.argv) < 2:
        print ("Please specify input csv file name")
        return

    csv_file_name = sys.argv[1]
    data = []
    with open(csv_file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data.append(list(row))

    train = resample(data[1:], replace=True, n_samples=int(len(data)))
    test = [x for x in data[1:] if x not in train]
    tree = dtree_build.buildtree(train, min_gain =0.01, min_samples = 5)

    # dtree_build.printtree(tree, '', col_names)
    # max_tree_depth = dtree_build.max_depth(tree)
    # print("max number of questions=" + str(max_tree_depth))

    right = 0
    pred_output = [['instance\#', 'actual', 'predicted', 'probability']]
    count = 1
    for x in test:
        temp = [count, x[-1]]
        temp.append
        result = dtree_build.classify(x, tree)
        total = 0
        for v in result.values():
            total += v
        maxv = 0
        maxk = ''
        for k, v in result.items():
            if v >= maxv:
                maxv = v
                maxk = k
        temp.append(maxk)
        temp.append(maxv/total)
        try:
            if float(result[x[-1]]/total) >= 0.5:
                right += 1
            else:
                pass
        except:
            pass
        pred_output.append(temp)
        count += 1

    with open("predicted.csv", "w") as output:
        writer = csv.writer(output)
        writer.writerows(pred_output)
    print("Accuracy for decision tree is",right/len(test))


if __name__ == "__main__":
    col_names = ['ZIP_CODE', 'TOTAL_VISITS', 'TOTAL_SPENT', 'HAS_CREDIT_CARD', 'AVRG_SPENT_PER_VISIT', 'PSWEATERS', 'PKNIT_TOPS', 'PKNIT_DRES', 'PBLOUSES', 'PJACKETS',
                'PCAR_PNTS', 'PCAS_PNTS', 'PSHIRTS', 'PDRESSES', 'PSUITS', 'POUTERWEAR', 'PJEWELRY', 'PFASHION', 'PLEGWEAR',
                 'PCOLLSPND', 'AMSPEND', 'PSSPEND', 'CCSPEND', 'AXSPEND', 'SPEND_LAST_MONTH', 'SPEND_LAST_3MONTH',
                 'SPEND_LAST_6MONTH', 'SPENT_LAST_YEAR', 'GMP', 'PROMOS_ON_FILE', 'DAYS_ON_FILE', 'FREQ_DAYS', 'MARKDOWN',
                 'PRODUCT_CLASSES', 'COUPONS', 'STYLES', 'STORES', 'STORELOY', 'VALPHON', 'WEB', 'MAILED', 'RESPONDED', 'RESPONSERATE', 'LTFREDAY', 'CLUSTYPE', 'PERCRET']
    main(col_names)
