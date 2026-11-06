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


def bt_dang14_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Random số điểm thí sinh đạt được ở Phần 2
                # Các mức điểm có thể có cho 1 câu ở Phần 2: 0; 0,1; 0,25; 0,5; 1
                muc_diem_p2 = [0, 0.1, 0.25, 0.5, 1.0]
                p2_c1 = random.choice(muc_diem_p2)
                p2_c2 = random.choice(muc_diem_p2)
                p2_c3 = random.choice(muc_diem_p2)
                p2_c4 = random.choice(muc_diem_p2)

                tong_diem_p2 = round(p2_c1 + p2_c2 + p2_c3 + p2_c4, 2)

                # 2. Ngưỡng điểm tổng bài thi (thường từ 2,5 đến 3,5 để xác suất rơi vào 10^-8)
                nguong_diem = random.choice([2.75, 3.0, 3.25])

                # 3. Tính toán số câu đúng tối thiểu ở Phần 1
                # Phần 3 là 0 điểm. P1 + P2 > nguong_diem => P1 > nguong_diem - tong_diem_p2
                diem_can_p1 = round(nguong_diem - tong_diem_p2, 2)
                # Mỗi câu P1 được 0.25 điểm
                k_min = math.ceil(diem_can_p1 / 0.25 + 0.000001) # cộng sai số nhỏ để tránh lỗi làm tròn

                if k_min > 12: k_min = 12 # Giới hạn nếu điểm quá cao
                if k_min < 8: k_min = 9    # Giới hạn để bài toán không quá dễ

                # 4. Tính xác suất P = P(X >= k_min) với X ~ B(12, 0.25)
                prob = 0
                list_trinh_bay_xs = []
                for k in range(k_min, 13):
                    # P(X=k) = C(12, k) * (0.25^k) * (0.75^(12-k))
                    p_k = binomial(12, k) * (Decimal('0.25')**k) * (Decimal('0.75')**(12-k))
                    prob += p_k
                    if k < 12:
                        list_trinh_bay_xs.append(f"P_{{{k}}} = 0,25^{{{k}}} \\cdot 0,75^{{{12-k}}} \\cdot C_{{12}}^{{{k}}}")
                    else:
                        list_trinh_bay_xs.append(f"P_{{{12}}} = 0,25^{{12}}")

                # 5. Tính x = P * 10^8
                x_val = prob * Decimal('100000000')
                phan_nguyen_x = int(x_val)

                # 6. Tính tổng các chữ số của phần nguyên x
                kq_dung = sum(int(digit) for digit in str(phan_nguyen_x))

                # Các đáp án trắc nghiệm
                da = kq_dung
                s = [da + 1, da + 2, da + 5, da - 1, da - 2, da - 3]
                s = [i for i in s if i > 0] # Đảm bảo đáp án dương

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Trong kỳ thi tốt nghiệp THPT năm 2025 có môn thi bắt buộc là môn Toán. Cấu trúc đế thi môn toán gồm 22 câu với ba phần như sau:\\\\
            + Phần 1: 12 câu hỏi ở dạng thức trắc nghiệm nhiều lựa chọn, mỗi câu cho 04 phương án trả lời trong đó có 01 phương án là đáp án đúng;\\\\
            + Phần 2: 04 câu hỏi ở dạng thức trắc nghiệm dạng Đúng/Sai. Mỗi câu hỏi có 04 ý, tại mỗi ý thí sinh lựa chọn đúng hoặc sai;\\\\
            + Phần 3: 06 câu hỏi ở dạng thức trắc nghiệm dạng trả lời ngắn. Thí sinh ghi và tô vào các ô tương ứng với đáp án của mình.\\\\
            Phần 1: Mỗi câu trả lời đúng được 0,25 điểm.\\\\
            Phần 2: + Chỉ lựa chọn chính xác 01 ý trong 01 câu hỏi được 0,1 điểm;\\\\
            + Chỉ lựa chọn chính xác 02 ý trong 01 câu hỏi được 0,25 điểm;\\\\
            + Chỉ lựa chọn chính xác 03 ý trong 01 câu hỏi được 0,5 điểm;\\\\
            + Chính xác cả 04 ý trong 01 câu hỏi được 1 điểm.\\\\
            Phần 3: Mỗi câu trả lời đúng được 0,5 điểm.\\\\
            Giả sử một thí sinh do lười học nên không làm được môn toán. Phần 3 thí sinh không trả lời đúng câu nào. Phần 1 và phần 2 thí sinh tô bừa các đáp án. Nếu thí sinh tô phần 2 được tổng $%s$ điểm. Khi đó xác suất của 12 câu tô bừa ở phần 1 để tổng điểm bài làm môn toán của thí sinh được trên $%s$ điểm là $x \\cdot 10^{-8}$. Tổng các chữ số phần nguyên của $x$ bằng bao nhiêu?'''
                                 %(str(tong_diem_p2).replace('.', ','), str(nguong_diem).replace('.', ',')))

                # Nội dung lời giải
                # Chuỗi trình bày các trường hợp
                loigiai_cac_th = ""
                for idx, k in enumerate(range(k_min, 13)):
                    loigiai_cac_th += f"Trường hợp {idx+1}: Số câu đúng ở phần 1 là {k} câu. Khi đó xác suất là ${list_trinh_bay_xs[idx]}$. \\\\ "

                loigiai = ('''Để tổng điểm bài làm môn toán của thí sinh được trên $%s$ điểm thì số điểm ở phần 1 phải lớn hơn $%s - %s = %s$ điểm. 
            Vì mỗi câu trả lời đúng phần 1 được 0,25 điểm nên số câu trả lời đúng $k$ sẽ thỏa mãn $k \\cdot 0,25 > %s \\Rightarrow k \\ge %s$. \\\\
            %s
            Vậy xác suất cần tìm là $P = \\sum_{i=%s}^{12} P_i \\approx %s \\cdot 10^{-8}$. \\\\
            Do đó phần nguyên của $x$ là %s. Vậy tổng các chữ số phần nguyên của $x$ bằng %s.'''
                           %(str(nguong_diem).replace('.', ','), 
                             str(nguong_diem).replace('.', ','), 
                             str(tong_diem_p2).replace('.', ','), 
                             str(diem_can_p1).replace('.', ','),
                             str(diem_can_p1).replace('.', ','), 
                             str(k_min), 
                             loigiai_cac_th, 
                             str(k_min), 
                             str(x_val).replace('.', ','), 
                             str(phan_nguyen_x), 
                             str(da)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(str(da))
                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

