import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang61_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tập hợp gồm 7 số liên tiếp
                start = random.randint(1, 10)
                X = [start + i for i in range(7)]
                X_str = "; ".join(map(str, X))
                S_X = sum(X)

                # 3 giá trị x duy nhất có thể ở tâm
                x_vals = [X[0], X[3], X[6]]

                # Random câu hỏi: chẵn hoặc lẻ
                parity_target = random.choice(['lẻ', 'chẵn'])
                valid_x = [x for x in x_vals if (x % 2 != 0 if parity_target == 'lẻ' else x % 2 == 0)]
                num_valid = len(valid_x)

                # Tính số cách và xác suất
                n_A = num_valid * 48
                n_omega = 144

                from fractions import Fraction
                f = Fraction(n_A, n_omega)
                if f.denominator == 1:
                    frac_latex = f"{f.numerator}"
                else:
                    frac_latex = f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

                dec = Decimal(float(n_A) / n_omega).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                dec_str = str(dec).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % dec_str]
                da = du[0]

                # Sinh các phương án sai
                pool = ["0,33", "0,67", "0,50", "0,25", "0,75", "0,45", "0,60", "0,40"]
                if dec_str in pool:
                    pool.remove(dec_str)
                random.shuffle(pool)
                s_list = pool[:3]
                das1 = '$%s$' % s_list[0]
                das2 = '$%s$' % s_list[1]
                das3 = '$%s$' % s_list[2]

                # Hàm hỗ trợ tìm các cặp ghép cho lời giải
                def get_pairs_str(x_val, X_list):
                    rem = [v for v in X_list if v != x_val]
                    k = (sum(X_list) - x_val) // 3
                    pairs = []
                    used = set()
                    for v in rem:
                        if v not in used and (k - v) in rem and (k - v) != v:
                            pairs.append((min(v, k-v), max(v, k-v)))
                            used.add(v)
                            used.add(k-v)
                    pairs.sort()
                    pairs_str = ", ".join([f"({p[0]}; {p[1]})" for p in pairs])
                    rem_str = "; ".join(map(str, rem))
                    return pairs_str, k, rem_str

                pairs1, k1, rem1 = get_pairs_str(x_vals[0], X)
                pairs2, k2, rem2 = get_pairs_str(x_vals[1], X)
                pairs3, k3, rem3 = get_pairs_str(x_vals[2], X)

                if num_valid == 1:
                    n_A_eq_str = "48"
                else:
                    n_A_eq_str = "48 + 48 = 96"

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Cho tập hợp $X = \\{%s\\}$. Người ta xếp ngẫu nhiên các chữ số từ tập $X$ vào các ô tròn như hình vẽ dưới đây sao cho mỗi ô chứa đúng một số. Biết rằng tổng của ba số trên mỗi đường thẳng đi qua tâm (ô tròn chính giữa) đều bằng nhau. Tính xác suất để số nằm ở ô chính giữa là một số %s? (Kết quả làm tròn đến hàng phần trăm).}
                {\\begin{tikzpicture}[scale=0.8, line width=1pt]
                    \\foreach \\angle in {30, 90, 150, 210, 270, 330} {
                        \\coordinate (V\\angle) at (\\angle:2.5); }
                    \\coordinate (C) at (0,0);
                    \\draw[red, thick] (V30) -- (V90) -- (V150) -- (V210) -- (V270) -- (V330) -- cycle;
                    \\draw[dashed, thick] (V90) -- (V270);
                    \\draw[dashed, thick] (V150) -- (V330);
                    \\draw[dashed, thick] (V30) -- (V210);
                    \\filldraw[fill=white, draw=blue, thick] (C) circle (0.45);
                    \\foreach \\angle in {30, 90, 150, 210, 270, 330} {
                        \\filldraw[fill=white, draw=blue, thick] (V\\angle) circle (0.45);}
                \\end{tikzpicture}}''' % (X_str, parity_target))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[scale=0.8, line width=1pt]
                    \\foreach \\angle/\\name in {90/a, 30/b, 330/c, 270/d, 210/e, 150/f} {
                        \\coordinate (V\\name) at (\\angle:2.5); }
                    \\coordinate (C) at (0,0);
                    \\draw[red, thick] (Va) -- (Vb) -- (Vc) -- (Vd) -- (Ve) -- (Vf) -- cycle;
                    \\draw[dashed, thick] (Va) -- (Vd);
                    \\draw[dashed, thick] (Vf) -- (Vc);
                    \\draw[dashed, thick] (Vb) -- (Ve);
                    \\filldraw[fill=white, draw=blue, thick] (C) circle (0.45) node[black] {$x$};
                    \\foreach \\name in {a,b,c,d,e,f} {
                        \\filldraw[fill=white, draw=blue, thick] (V\\name) circle (0.45) node[black] {$\\name$}; }
                \\end{tikzpicture}
                \\end{center}
                Gọi số nằm giữa là $x \\in X = \\{%s\\}$ và các số bên ngoài được minh họa như hình vẽ\\\\
                Các cặp số đối xứng qua tâm trên cùng một đường thẳng là $(a;d), (b;e), (c;f)$\\\\
                Tổng ba số trên mỗi đường thẳng đi qua tâm bằng nhau gọi là $T$, khi đó ta có:\\\\
                $T = a+x+d = b+x+e = c+x+f \\Leftrightarrow a+d = b+e = c+f = k$\\\\
                Tổng của các số trong tập $X$ là: $S_X = %s$\\\\
                Tổng của 3 đường thẳng đi qua tâm là $3T$. Khi cộng tổng 3 đường thẳng này, số ở tâm là $x$ được tính 3 lần, còn các số ở vòng ngoài được tính 1 lần.\\\\
                Khi đó ta có: $3T = S_X + 2x \\Leftrightarrow 3T = %s + 2x$. Để tồn tại cách xếp thì vế phải là $(%s + 2x)$ phải chia hết cho $3$ nên $x \\in \\{%s; %s; %s\\}$\\\\
                \\textbf{Trường hợp 1:} $x = %s$\\\\
                Tổng cặp bên ngoài $k = \\frac{%s - %s}{3} = %s$ nên khi đó tập còn lại $\\{%s\\}$ thì các cặp có tổng bằng $%s$ là: $%s$\\\\
                Hoán vị 3 cặp vào 3 đường thẳng: $3! = 6$ cách, hoán vị vị trí 2 số trong mỗi cặp có $2^3 = 8$ cách.\\\\
                Tổng số cách: $6 \\cdot 8 = 48$ cách.\\\\
                \\textbf{Trường hợp 2:} $x = %s$\\\\
                Tổng cặp bên ngoài $k = \\frac{%s - %s}{3} = %s$ nên khi đó tập còn lại $\\{%s\\}$ thì các cặp có tổng bằng $%s$ là: $%s$\\\\
                Số cách xếp cũng tương tự trường hợp 1 có $3! \\cdot 2^3 = 48$ cách.\\\\
                \\textbf{Trường hợp 3:} $x = %s$\\\\
                Tổng cặp bên ngoài $k = \\frac{%s - %s}{3} = %s$ nên khi đó tập còn lại $\\{%s\\}$ thì các cặp có tổng bằng $%s$ là: $%s$\\\\
                Số cách xếp tương tự có: $3! \\cdot 2^3 = 48$ cách.\\\\
                Tổng số cách xếp thỏa mãn điều kiện đề bài: $n(\\Omega) = 48 + 48 + 48 = 144$ (cách)\\\\
                Số cách xếp mà tâm $x$ là số %s: $n(A) = %s$\\\\
                Vậy xác suất cần tìm là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{144} = %s \\approx %s$''' %
                    (X_str, S_X, S_X, S_X, x_vals[0], x_vals[1], x_vals[2],
                    x_vals[0], S_X, x_vals[0], k1, rem1, k1, pairs1,
                    x_vals[1], S_X, x_vals[1], k2, rem2, k2, pairs2,
                    x_vals[2], S_X, x_vals[2], k3, rem3, k3, pairs3,
                    parity_target, n_A_eq_str, n_A, frac_latex, dec_str))
                dapan='\\shortans[0]{$%s$}\n'%(dec_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

