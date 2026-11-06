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


def bt_dang63_p3_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số chàng trai (n) và số chia cuối cùng (K)
                n = random.choice([5, 6, 7])

                # Tính số nghiệm cho từng trường hợp
                P0 = sum([(n - b + 1) for b in range(1, n + 1)])
                P1 = sum([(n - 1 - b + 1) for b in range(1, n)])
                P2 = sum([(n - 2 - b + 1) for b in range(1, n - 1)])

                P_total = P0 + P1 + P2
                n_fact = math.factorial(n)
                T = P_total * n_fact

                # Đảm bảo T chia hết cho K để kết quả luôn là số nguyên đẹp
                valid_K = [k for k in [40, 50, 60, 80, 100, 120] if T % k == 0]
                K = random.choice(valid_K)
                ans = T // K

                # Hàm tạo bảng số liệu Latex cho các trường hợp
                def get_table(c_val, n_boys):
                    target = n_boys - c_val
                    rows = ""
                    for b in range(1, target + 1):
                        ad = target - b
                        ways = ad + 1
                        rows += "            " + str(b) + " & " + str(ad) + " & " + str(ways) + " \\\\ \\hline\n"

                    table = (
                        "\\begin{center}\n"
                        "\\renewcommand{\\arraystretch}{1.2}\n" # Tăng chiều cao của các hàng cho thoáng
                        "\\begin{tabular}{|c|c|c|}\n"
                        "\\hline\n"
                        "            \\hspace{0.8cm} $b$ \\hspace{0.8cm} & \\hspace{0.8cm} $a+d$ \\hspace{0.8cm} & \\hspace{0.5cm} \\textbf{Số nghiệm} \\hspace{0.5cm} \\\\ \\hline\n"
                        + rows +
                        "\\end{tabular}\n"
                        "\\end{center}"
                    )
                    return table

                # Hàm tạo chuỗi tập hợp b
                def set_str(end):
                    return "\\{" + "; ".join(str(i) for i in range(1, end + 1)) + "\\}"

                tab0 = get_table(0, n)
                tab1 = get_table(1, n)
                tab2 = get_table(2, n)

                # Các đáp án trắc nghiệm
                da = str(ans)
                wrong_offsets = [1, -1, 2, -2, 10, -10, 20, -20]
                s_list = []
                for offset in wrong_offsets:
                    w_val = ans + offset
                    if w_val > 0 and w_val != ans:
                        s_list.append(str(w_val))

                # Lọc trùng và lấy ngẫu nhiên 3 phương án sai
                s_list = list(set(s_list))
                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Tiến hành xếp $3$ cô gái ($G_1; G_2; G_3$) và $%s$ chàng trai vào $%s$ chiếc ghế hàng ngang sao cho ba cô gái ngồi theo đúng thứ tự $G_1; G_2; G_3$ từ trái sang phải (không nhất thiết phải ngồi kề nhau). Giữa cô gái thứ nhất ($G_1$) và cô gái thứ hai ($G_2$) có ít nhất một chàng trai, giữa cô gái thứ hai ($G_2$) và cô gái thứ ba ($G_3$) có tối đa hai chàng trai. Gọi $T$ là số cách xếp thỏa mãn. Giá trị $\\frac{T}{%s}$ bằng bao nhiêu?''' 
                                 % (n, n + 3, K))

                # Lời giải
                loigiai = ('''Gọi $a$ là số chàng trai đứng trước cô gái thứ nhất $G_1$ ($a \\ge 0$). \\\\
            $b$ là số chàng trai ở giữa cô gái thứ nhất và cô gái thứ hai $G_1 - G_2$ ($b \\ge 1$). \\\\
            $c$ là số chàng trai ở giữa cô gái thứ hai và cô gái thứ ba $G_2 - G_3$ ($c \\in \\{0; 1; 2\\}$). \\\\
            $d$ là số chàng trai đứng sau cô gái thứ ba $G_3$ ($d \\ge 0$). \\\\
            Do có $%s$ chàng trai nên $a + b + c + d = %s$. \\\\
            \\textbf{Trường hợp 1:} Với $c = 0$ suy ra $a + b + d = %s$ ($b \\ge 1$) nên $b \\in %s$.
            %s
            Vậy tổng số nghiệm trong trường hợp này bằng $%s$. \\\\
            \\textbf{Trường hợp 2:} Với $c = 1$ suy ra $a + b + d = %s$ ($b \\ge 1$) nên $b \\in %s$.
            %s
            Vậy tổng số nghiệm trong trường hợp này bằng $%s$. \\\\
            \\textbf{Trường hợp 3:} Với $c = 2$ suy ra $a + b + d = %s$ ($b \\ge 1$) nên $b \\in %s$.
            %s
            Vậy tổng số nghiệm trong trường hợp này bằng $%s$. \\\\
            Số cách chia $%s$ chàng trai vào $4$ khoảng trống: $%s + %s + %s = %s$ cách. \\\\
            Số cách xếp $%s$ chàng trai này là $%s! = %s$ cách. \\\\
            Vậy số cách xếp thỏa mãn là: $T = %s \\cdot %s = %s$ nên $\\frac{T}{%s} = \\frac{%s}{%s} = %s$.''' % (
                    n, n, 
                    n, set_str(n), tab0, P0,
                    n-1, set_str(n-1), tab1, P1,
                    n-2, set_str(n-2), tab2, P2,
                    n, P0, P1, P2, P_total,
                    n, n, n_fact,
                    P_total, n_fact, T, K, T, K, ans
                ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
                dapan='\\shortans[0]{$%s$}\n'%(ans)    
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

