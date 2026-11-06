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


def bt_dang64_p3_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # H luôn cố định là 1! * 2! * 3! * 4! * 5! = 34560 với lưới hình này.
                # Ta sẽ random tập hợp S bằng cách xáo trộn số lượng phần tử của các nhóm số dư.
                P = [1, 2, 3, 4, 5]
                random.shuffle(P)

                S_list = []
                A_lists = {}
                for rem in range(5):
                    count = P[rem]
                    A_lists[rem] = [rem + 5*i for i in range(count)]
                    S_list.extend(A_lists[rem])

                S_list.sort()

                # Tạo chuỗi tập hợp dạng LaTeX
                S_str = '\\{' + '; '.join(map(str, S_list)) + '\\}'
                A0_str = '\\{' + '; '.join(map(str, A_lists[0])) + '\\}'
                A1_str = '\\{' + '; '.join(map(str, A_lists[1])) + '\\}'
                A2_str = '\\{' + '; '.join(map(str, A_lists[2])) + '\\}'
                A3_str = '\\{' + '; '.join(map(str, A_lists[3])) + '\\}'
                A4_str = '\\{' + '; '.join(map(str, A_lists[4])) + '\\}'

                # Random giá trị k để tính H/k
                k_list = [20, 24, 30, 32, 36, 40, 45, 48, 60, 64, 72, 80, 90, 96, 120]
                k = random.choice(k_list)

                kq_val = 34560 // k

                # Các đáp án trắc nghiệm
                da = kq_val
                # Tạo phương án nhiễu (sai khác số nguyên, đảm bảo > 0)
                s_raw = [da + 12, da - 12, da + 24, da - 24, da + 36, da - 36, da + 48, da - 48, da + 15, da - 15]
                s_valid = [x for x in s_raw if x > 0]
                s_choices = random.sample(s_valid, 3)

                # Câu hỏi
                noidungcauhoi = ('''Trong một trò chơi bạn Bình cần vượt qua một thử thách. Theo yêu cầu của thử thách, Bình cần điền tất cả $15$ số thuộc tập hợp $S = %s$ vào $15$ ô vuông trong hình dưới thỏa mãn đồng thời ba điều kiện sau: \\\\
            - Mỗi ô điền đúng một số và mỗi số chỉ được sử dụng một lần; \\\\
            - Hiệu hai số ở hai ô bất kì khác nhau trên cùng một hàng không chia hết cho $5$; \\\\
            - Hiệu hai số ở hai ô bất kì khác nhau trên cùng một cột không chia hết cho $5$. \\\\
            Hai cách điền gọi là giống nhau nếu số điền ở mỗi ô tương ứng trong $15$ ô là giống nhau (không tính đến thứ tự điền các số vào $15$ ô vuông). Gọi $H$ là số cách điền khác nhau để bạn Bình vượt qua được thử thách. Giá trị của $\\frac{H}{%s}$ bằng bao nhiêu?
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt]
            \\draw (0,0) grid (5,1);
            \\draw (0,1) grid (4,2);
            \\draw (0,2) grid (3,3);
            \\draw (0,3) grid (2,4);
            \\draw (0,4) grid (1,5);
            \\node at (-1, 0.5) {Hàng 1};
            \\node at (-1, 1.5) {Hàng 2};
            \\node at (-1, 2.5) {Hàng 3};
            \\node at (-1, 3.5) {Hàng 4};
            \\node at (-1, 4.5) {Hàng 5};
            \\node[font=\\footnotesize] at (0.5, -0.5) {Cột1};
            \\node[font=\\footnotesize] at (1.5, -0.5) {Cột2};
            \\node[font=\\footnotesize] at (2.5, -0.5) {Cột3};
            \\node[font=\\footnotesize] at (3.5, -0.5) {Cột4};
            \\node[font=\\footnotesize] at (4.5, -0.5) {Cột5};
            \\end{tikzpicture}
            \\end{center}''' % (S_str, k))

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % s_choices[0])
                da_s2 = ('$%s$' % s_choices[1])
                da_s3 = ('$%s$' % s_choices[2])

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Chia các phần tử của tập hợp $S$ thành $5$ nhóm theo số dư khi chia cho $5$: \\\\
            - Nhóm $R_0$ (chia hết cho $5$): $%s$ gồm $%s$ phần tử. \\\\
            - Nhóm $R_1$ (chia $5$ dư $1$): $%s$ gồm $%s$ phần tử. \\\\
            - Nhóm $R_2$ (chia $5$ dư $2$): $%s$ gồm $%s$ phần tử. \\\\
            - Nhóm $R_3$ (chia $5$ dư $3$): $%s$ gồm $%s$ phần tử. \\\\
            - Nhóm $R_4$ (chia $5$ dư $4$): $%s$ gồm $%s$ phần tử. \\\\
            Điều kiện "hiệu hai số cùng hàng/cột không chia hết cho $5$" tương đương với việc "không có hai số nào cùng hàng hoặc cùng cột có cùng số dư khi chia cho $5$". \\\\
            Giả sử các ô trong bảng có tọa độ $(i,j)$ với $i$ là vị trí hàng (tính từ dưới lên), $j$ là vị trí cột (tính từ trái sang). Bảng gồm $15$ ô. \\\\
            Nhận xét rằng, số lượng ô trên các đường chéo phụ (tập hợp các ô thỏa mãn $i+j = c$) lần lượt là $1, 2, 3, 4, 5$ (ứng với $c = 2, 3, 4, 5, 6$). \\\\
            Để không có hai số nào cùng hàng hoặc cùng cột có cùng số dư khi chia cho $5$, các số thuộc cùng một nhóm số dư bắt buộc phải được xếp vào cùng một đường chéo phụ có số lượng ô tương ứng. \\\\
            Cụ thể, nhóm có kích thước $5$ bắt buộc phải nằm ở đường chéo có $5$ ô. Sau đó nhóm có kích thước $4$ bắt buộc phải nằm ở đường chéo có $4$ ô, v.v... Cuối cùng nhóm có kích thước $1$ nằm ở đường chéo có $1$ ô. \\\\
            Do đó, số cách xếp các số vào bảng chính là tích của số cách hoán vị các số trong từng nhóm số dư riêng biệt. \\\\
            Số cách điền thỏa mãn thử thách là: $H = 1! \\cdot 2! \\cdot 3! \\cdot 4! \\cdot 5! = 1 \\cdot 2 \\cdot 6 \\cdot 24 \\cdot 120 = 34560$ (cách). \\\\
            Vậy giá trị của $\\frac{H}{%s} = \\frac{34560}{%s} = %s$.'''
                           % (A0_str, P[0], A1_str, P[1], A2_str, P[2], A3_str, P[3], A4_str, P[4], k, k, kq_val))
                dapan='\\shortans[0]{$%s$}\n'%(kq_val)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content 

