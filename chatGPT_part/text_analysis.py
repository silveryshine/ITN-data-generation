import os
import string

import jiwer

import GPT_utils
import cal_wer


def sentence_wer_check(reference_dir:str, input_dir:str, output_dir:str):
    # structed_file_path = os.path.join(input_dir, "structured.txt")
    structured_file_name = GPT_utils.google_dataset_preprocess(input_dir, output_dir, False)
    structured_file_path = os.path.join(output_dir, structured_file_name[-1])
    # structed_path =
    #reference_list = [[],[],[]]
    structured_list = []
    with open(structured_file_path, 'r', encoding='utf-8') as ref_fp:
        structured_list = ref_fp.readlines()

    completed_file_path = os.path.join(input_dir, "completed.txt")
    completed_list = []
    with open(completed_file_path, 'r', encoding='utf-8') as comp_fp:
        completed_list = [x.strip() for x in comp_fp.readlines()]

    reference_list = []
    for file_name in os.listdir(reference_dir):
        if file_name not in completed_list:
            continue
        file_path = os.path.join(reference_dir, file_name)
        with open(file_path, 'r', encoding="utf-8") as fp:
            lines = fp.readlines()
            reference_list.extend(lines)

    ref_idx = 0
    structured_length = len(structured_list)
    ref_length = len(reference_list)
    wer_value = 0
    actual_cnt = 0
    bf1 = 0
    flag = True
    bad_cnt = 0
    for idx,line in enumerate(structured_list):
        line_split = line.lower().strip().split("|||")
        if idx == 177:
            a = 1
        bf1 = ref_idx
        while(ref_idx < ref_length):
            reference_line_to_comp = reference_list[ref_idx].lower().strip().split("|||")[1].translate(str.maketrans('', '', string.punctuation)).split()
            hyp_line_to_comp = line_split[1].translate(str.maketrans('', '', string.punctuation)).split()
            if reference_line_to_comp[0] == hyp_line_to_comp[0]: #or reference_line_to_comp[-1] == hyp_line_to_comp[-1]:
                break
            ref_idx += 1
            if ref_idx - bf1 > 10:
                print(idx)
                print(line_split[1], end="\n")
                print(reference_list[bf1].lower().strip().split("|||")[1])
                print()
                flag = False
                ref_idx = bf1
                bad_cnt += 1
                break
        if ref_idx == ref_length:
            break
        if flag is False:
            flag = True
            continue
        line_split = line.lower().strip().split("|||")
        ref_split = reference_list[ref_idx].lower().strip().split("|||")

        single_wer = jiwer.compute_measures(ref_split[0], line_split[0])['wer']
        # if single_wer > 0.5:
        #     print(str(idx) + " " + ref_split[1] + " ||| " +line_split[1])
        wer_value += single_wer
        ref_idx += 1
        actual_cnt += 1
    print(wer_value/structured_length)
    print(actual_cnt)
    print("bad cnt = " + str(bad_cnt))





    pass


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--json", required=True)
    # args = parser.parse_args()
    #
    # with open(args.json, "r") as j_obj:
    #     config = json.load(j_obj)

    config = {
        "text_generate": {
            "api_key": "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",
            # "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",   # "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"
            "input_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\youtube_crawler\\Chris@HoneyMoneySG\\segmented_text_with_times",
            "output_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\youtube_crawler\\Chris@HoneyMoneySG\\chatGPT"
        },
        "preprocess": {
            "input_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\google_text_normalization_dataset\\en_with_types",
            "output_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\google_text_normalization_dataset\\en_with_types_sentence",
            "log": ""
        },
        "text_analysis": {
            "reference_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\google_text_normalization_dataset\\en_with_types_sentence",
            "input_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\google_text_normalization_dataset\\en_with_types_sentence_ChatGPT",
            "output_dir": "D:\\study\\singaporeMasters\\master_project\\term2\\data\\google_text_normalization_dataset\\en_with_types_sentence_ChatGPT_analysis"
        }
    }
    sentence_wer_check(config["text_analysis"]["reference_dir"], config["text_analysis"]["input_dir"], config["text_analysis"]["output_dir"])
    pass


if __name__ == "__main__":
    main()