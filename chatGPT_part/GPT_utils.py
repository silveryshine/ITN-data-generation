import os

def google_dataset_preprocess(input_dir:str, output_dir:str, separated=True):
    file_names = []
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        with open(file_path, 'r') as in_fp: #, encoding='utf-8'
            lines =  in_fp.readlines()
            out_fp = None
            cnt_file = 0
            cnt = 0
            spoken = []
            written = []
            type = []
            out_fp = open(os.path.join(output_dir, file_name + "-" + str(cnt_file).zfill(7)), 'w', encoding='utf-8')
            file_names.append(file_name + "-" + str(cnt_file).zfill(7))
            for line in lines:
                line_split = line.split('\t')
                if len(line_split) == 2 and line_split[0] == "<eos>":
                    cnt += 1
                    out_fp.write(" ".join(written) + " ||| " + " ".join(spoken) + " ||| " + " ".join(type) + "\n")
                    spoken.clear()
                    written.clear()
                    type.clear()
                    if cnt % 50 == 0 and separated is True:
                        out_fp.close()
                        cnt_file += 1
                        out_fp = open(os.path.join(output_dir, file_name + "-" + str(cnt_file).zfill(7)), 'w', encoding='utf-8')
                        file_names.append(file_name + "-" + str(cnt_file).zfill(7))
                    continue
                if len(line_split) == 3:
                    if line_split[0] == "PLAIN" or line_split[0] == "PUNCT":
                        line_split[2] = line_split[1]
                    written.append(line_split[1].strip())
                    spoken.append(line_split[2].strip())
                    type.append(line_split[0].strip())
        out_fp.close()

        # break
    return file_names




def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--json", required=True)
    # args = parser.parse_args()
    #
    # with open(args.json, "r") as j_obj:
    #     config = json.load(j_obj)

    config = {
        "text_generate": {
            "api_key": "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", #"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",   # "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"
            "input_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\youtube_crawler\\Chris@HoneyMoneySG\\segmented_text_with_times",
            "output_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\youtube_crawler\\Chris@HoneyMoneySG\\chatGPT"
        },
        "preprocess": {
            "input_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\google_text_normalization_dataset\\en_with_types",
            "output_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\google_text_normalization_dataset\\en_with_types_sentence",
            "log":""
        }
    }

    google_dataset_preprocess(config["preprocess"]["input_dir"], config["preprocess"]["output_dir"])
    pass


if __name__ == "__main__":
    main()