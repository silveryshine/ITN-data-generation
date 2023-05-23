import os

## generate files for word alignment training.
def generate_train_file():
    infile_dir_path = r"D:\study\singaporeMasters\master_project\term2\data\google_text_normalization_dataset\en_with_types"
    outfile_dir_path = r"D:\study\singaporeMasters\master_project\term2\data\google_text_normalization_dataset\en_sentence"
    infile_dir_path = r"D:\study\singaporeMasters\master_project\term2\data\google_text_normalization_dataset\en_with_types_split\test"
    limit = 5
    cnt = 0
    outfile_name = "test.itn-tn"
    outtlapfile_name = "itntn.talp"
    out_fp = open(os.path.join(outfile_dir_path, outfile_name), 'w+', encoding='utf-8')
    outtlap_fp = open(os.path.join(outfile_dir_path, outtlapfile_name), 'w+', encoding='utf-8')
    for file_name in os.listdir(infile_dir_path):
        if cnt != 2:
            cnt += 1
            continue
        if cnt == limit:
            break
        cnt += 1
        with open(os.path.join(infile_dir_path, file_name), 'r+', encoding='utf-8') as in_fp:
            lines = in_fp.readlines()
            itn_str = ""
            tn_str = ""
            itn_idx = 1
            tn_idx = 1
            tlap_token = []
            for line in lines:
                line_split = line.split('\t')
                if line_split[0] == '<eos>':
                    out_fp.write(itn_str + '||| ' + tn_str + '\n')
                    outtlap_fp.write(' '.join(tlap_token) + '\n')
                    tlap_token = []
                    itn_str = ""
                    tn_str = ""
                    itn_idx = 1
                    tn_idx = 1
                elif line_split[2] == '<self>\n' or line_split[0] == 'PUNCT':
                    itn_str += line_split[1] + " "
                    tn_str += line_split[1] + " "
                    tlap_token.append(str(itn_idx) + '-' + str(tn_idx))
                    itn_idx += 1
                    tn_idx += 1
                else:
                    itn_str += line_split[1] + " "
                    tn_str += line_split[2][:-1] + " "
                    for i in range(len(line_split[2].split())):
                        tlap_token.append(str(itn_idx) + '-' + str(tn_idx))
                        tn_idx += 1
                    itn_idx += 1
    out_fp.close()
    outtlap_fp.close()
    pass


## generate result dataset using the paralleled sentence and generated alignment
def generate_alignment_tsv():
    data_dir_path = r"D:\study\singaporeMasters\master_project\term2\data\google_text_normalization_dataset\en_sentence\test"
    test_data = os.path.join(data_dir_path, "test_real.itn-tn")
    out_alignment = os.path.join(data_dir_path, "gizapp-itntn.out")

    out_file_fp = open(os.path.join(data_dir_path,"testout_real_gizapp.tsv"), "w+", encoding='utf-8')

    with open(test_data, 'r', encoding='utf-8') as test_fp, open(out_alignment, 'r', encoding='utf-8') as out_align_fp:
        test_lines = test_fp.readlines()
        out_align_lines = out_align_fp.readlines()

        last_itn_idx = -1
        last_tn_idx = -1
        idx_diff = 0
        for idx,test_line in enumerate(test_lines):
            test_line_split = test_line.split("|||")
            itn_sentence_split = test_line_split[0].split()
            tn_sentence_split = test_line_split[1].split()
            if len(itn_sentence_split) == 0:
                idx_diff -= 1
                continue
            align_split = out_align_lines[idx + idx_diff].split()

            for align_mark in align_split:
                align_mark_split = align_mark.split("-")
                align_itn = ' '.join(itn_sentence_split[last_itn_idx + 1: int(align_mark_split[0]) + 1])
                last_itn_idx = int(align_mark_split[0])
                align_tn = ' '.join(tn_sentence_split[last_tn_idx + 1: int(align_mark_split[1]) + 1])
                last_tn_idx = int(align_mark_split[1])
                out_file_fp.write(align_itn + '\t' + align_tn + '\n')
    out_file_fp.close()


## generate testset from youtube and wenet transcript
def generate_bitext_youtube_wenet():
    wenet_dir = r"D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\wenet_transcript"
    youtube_dir = r"D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\segmented_wav"
    out_dir = r"D:\study\singaporeMasters\master_project\term2\data\google_text_normalization_dataset\en_sentence"

    to_generate = []

    for url in os.listdir(youtube_dir):
        video_dir_path = os.path.join(youtube_dir, url)
        for file_name in os.listdir(video_dir_path):
            file_path = os.path.join(video_dir_path, file_name)
            if os.path.isdir(file_path):
                continue
            wenet_file = os.path.join(wenet_dir, file_name)
            if not os.path.exists(wenet_file):
                continue
            with open(wenet_file,'r') as wenet_fp, open(file_path, 'r') as youtube_fp:
                youtube_line = youtube_fp.readline()
                wenet_line = wenet_fp.readline()
                wenet_line = ' '.join(wenet_line.split()) #[3:]) no need for [3:] after rescue
                to_generate.append(youtube_line + " ||| " + wenet_line + '\n')
    with open(os.path.join(out_dir, 'test_real.itn-tn'), 'w+') as out_fp:
        out_fp.writelines(to_generate)


## for data regain
def rescue():
    wenet_dir = r"D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\wenet_transcript"
    youtube_dir = r"D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\segmented_wav"
    itn_dir =  r"D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\itn_dataset"
    for file_name in os.listdir(wenet_dir):
        if file_name.endswith("_timestamp.txt"):
            continue
        file_path = os.path.join(wenet_dir, file_name)
        timestamp_path = os.path.join(wenet_dir, file_name[:-4] + "_timestamp.txt")
        with open(file_path, 'w+') as transcipt_fp, open(timestamp_path, 'r') as timestamp_fp:
            lines = timestamp_fp.readlines()
            to_write_back = []
            for line in lines:
                to_write_back.append(line.split()[0])
            transcipt_fp.write(' '.join(to_write_back))

    for url in os.listdir(youtube_dir):
        video_dir_path = os.path.join(youtube_dir, url)
        for file_name in os.listdir(video_dir_path):
            itn_file_path = os.path.join(itn_dir, file_name)
            file_path = os.path.join(video_dir_path, file_name)
            if not os.path.exists(itn_file_path):
                continue
            with open(file_path, "w+") as file_fp, open(itn_file_path, 'r') as itn_fp:
                lines = itn_fp.readlines()
                to_write_back = []
                for line in lines:
                    to_write_back.append(line.split()[0])
                file_fp.write(' '.join(to_write_back))


def separate_itn_tn_text():
    data_dir_path = r"D:\study\singaporeMasters\master_project\term2\data\google_text_normalization_dataset\en_sentence\test"
    with open(os.path.join(data_dir_path, "test.itn-tn"), 'r', encoding='utf-8') as fp:
        with open(os.path.join(data_dir_path, "test_itn.txt"), 'w', encoding='utf-8') as itn_fp, \
                open(os.path.join(data_dir_path, "test_tn.txt"), 'w', encoding='utf-8') as tn_fp:
            lines = fp.readlines()
            for line in lines:
                line = line.strip().split(" ||| ")
                if len(line) < 2:
                    continue
                itn_fp.write(line[0] + '\n')
                tn_fp.write(line[1] + '\n')


def generate_talp_for_GIZA():
    file_path = r"D:\study\singaporeMasters\master_project\term2\data\google_text_normalization_dataset\en_sentence\test\test_real_GIZA.A3.final"
    result = []
    with open(file_path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        for line in lines:
            sub_result = []
            if line.startswith('#'):
                continue
            if not line.startswith('NULL'):
                continue
            line = line.strip()
            line = line.split("})")
            for idx,token in enumerate(line):
                if len(token) == 0:
                    continue
                token = token.split("({")
                word = token[0].strip()
                if len(token[1].strip()) == 0:
                    continue
                links = token[1].strip().split()
                if word == "NULL":
                    continue
                for link in links:
                    sub_result.append(str(idx-1) + '-' + str(int(link)-1))
            result.append(' '.join(sub_result) + '\n')
    with open(r"D:\study\singaporeMasters\master_project\term2\data\google_text_normalization_dataset\en_sentence\test\gizapp-itntn.out", 'w') as out_fp:
        out_fp.writelines(result)
        a = 1



if __name__ == '__main__':
    appp = [0,1,2,3]
    print(appp[:4])
    # main2()
    generate_alignment_tsv()
    # generate_bitext_youtube_wenet()
    # rescue()
    # separate_itn_tn_text()
    # generate_talp_for_GIZA()
    # generate_train_file()