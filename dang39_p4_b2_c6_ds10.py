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


def bt_dang39_p4_b2_c6_ds10(self):
            #Khai báo biến
            # B1 & B3: Nghiên cứu đề bài và thiết lập thông số random
            # Tạo 5 đoạn thẳng ngẫu nhiên (thường chọn khoảng cách để có nhiều trường hợp tam giác)
            a1 = random.randint(2, 4)
            d = random.randint(2, 3)
            lengths = [a1 + i * d for i in range(5)]

            # Số phần tử không gian mẫu C(5, 3)
            n_omega = 10 

            # B2: Tính toán lời giải dựa trên các giá trị ngẫu nhiên
            favorable_cases = []
            all_combinations = list(itertools.combinations(lengths, 3))

            for combo in all_combinations:
                side = sorted(combo)
                if side[0] + side[1] > side[2]:
                    favorable_cases.append(side)

            n_a = len(favorable_cases)
            xac_suat = Rational(n_a, n_omega)
            # Chuyển đổi xác suất sang dạng thập phân dùng dấu phẩy cho tiếng Việt
            xac_suat_decimal = str(float(n_a/10)).replace('.', ',')

            # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
            possible_ans = [Rational(i, 10) for i in range(1, 10)]
            if xac_suat in possible_ans:
                possible_ans.remove(xac_suat)

            random.shuffle(possible_ans)
            wrong_ans = [str(latex(ans)).replace('.', ',') for ans in possible_ans[:3]]
            da_dung_str = str(latex(xac_suat)).replace('.', ',')

            # Chuẩn bị nội dung hiển thị các đoạn thẳng
            ds_doan_thang = ", ".join(["%s \\text{ cm}" % (latex(x).replace('.', ',')) for x in lengths])

            # Định dạng các bộ ba cạnh với \left( \right) và ngắt dòng sau nhóm thứ 3
            formatted_cases = ["\\left(" + f"{c[0]} \\text{{ cm}}, {c[1]} \\text{{ cm}}, {c[2]} \\text{{ cm}}" + "\\right)" for c in favorable_cases]

            if n_a > 3:
                # Lấy 3 nhóm đầu, đóng môi trường $, ngắt dòng, rồi mở lại $
                dong_1 = ", ".join(formatted_cases[:3]) + ",$ \\\\ $"
                phan_con_lai = formatted_cases[3:]
                if len(phan_con_lai) > 1:
                    dong_2 = ", ".join(phan_con_lai[:-1]) + " \\text{ hoặc } " + phan_con_lai[-1]
                else:
                    dong_2 = phan_con_lai[0]
                cac_truong_hop = dong_1 + dong_2
            elif n_a > 1:
                cac_truong_hop = ", ".join(formatted_cases[:-1]) + " \\text{ hoặc } " + formatted_cases[-1]
            elif n_a == 1:
                cac_truong_hop = formatted_cases[0]
            else:
                cac_truong_hop = "không có trường hợp nào"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có 5 đoạn thẳng có độ dài lần lượt là $%s$. Lấy ngẫu nhiên 3 đoạn thẳng trong 5 đoạn thẳng trên. Tính xác suất để 3 đoạn lấy ra lập thành một tam giác.'''
                             % (ds_doan_thang))

            # Các đáp án
            da_d = ('\\True $' + da_dung_str + '$')
            da_s1 = '$' + wrong_ans[0] + '$'
            da_s2 = '$' + wrong_ans[1] + '$'
            da_s3 = '$' + wrong_ans[2] + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết (không viết tắt)
            loigiai = ('''Số phần tử của không gian mẫu là $n(\\Omega) = C_5^3 = 10$. \\\\
                         Gọi $A$ là biến cố "3 đoạn thẳng lấy ra lập thành một tam giác". \\\\
                         Để 3 đoạn thẳng lập thành một tam giác, tổng độ dài hai cạnh bất kỳ phải luôn lớn hơn độ dài cạnh còn lại. \\\\
                         Dựa vào các độ dài cho trước, các trường hợp thỏa mãn là: \\\\
                         $%s$. \\\\
                         Suy ra số phần tử của biến cố $A$ là $n(A) = %s$. \\\\
                         Vậy xác suất cần tìm là $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{10} = %s$.'''
                       % (cac_truong_hop, latex(n_a), latex(n_a), da_dung_str))

            # Xuất câu trắc nghiệm theo mẫu content yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

