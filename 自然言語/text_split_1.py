import MeCab
import ipadic
import os
from pathlib import Path

text = "吾輩は猫である"

dic_dir = Path(ipadic.DICDIR)
mecabrc_path = dic_dir / "mecabrc"

# Chuyển Path sang chuỗi chuẩn dấu / bằng .as_posix()
dic_dir_str = dic_dir.as_posix()
mecabrc_path_str = mecabrc_path.as_posix()

os.environ["MECABRC"] = str(mecabrc_path)

#chasen出力
t = MeCab.Tagger(f"-d {dic_dir_str} -r {mecabrc_path_str} -Ochasen")
result = t.parse(text)
print(result)
