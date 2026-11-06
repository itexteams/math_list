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


def bt_dang49_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random số lượng chữ số trong tập hợp (từ 6 đến 8 chữ số)
                n_elements = randint(6, 8)
                # Chọn một tập hợp các chữ số liên tiếp bắt đầu từ 1, 2 hoặc 3
                start_num = randint(1, 3)
                all_digits = list(range(start_num, start_num + n_elements))
                all_digits_str = ", ".join(map(str, all_digits))

                # Bước 2: Chọn ngẫu nhiên 2 chữ số d1, d2 phải đứng cạnh nhau
                d_pair = random.sample(all_digits, 2)
                d1, d2 = d_pair[0], d_pair[1]

                # Bước 3: Tính toán các giá trị
                # Số phần tử không gian mẫu n(Omega) = A(n, 3)
                n_omega = n_elements * (n_elements - 1) * (n_elements - 2)

                # Số kết quả thuận lợi n(A)
                # - Số cách chọn chữ số thứ 3: (n_elements - 2) cách
                # - Hoán vị d1, d2: 2! = 2 cách
                # - Hoán vị cụm {d1, d2} với chữ số còn lại: 2! = 2 cách
                n_remain = n_elements - 2
                n_A = 2 * n_remain * 2

                # Xác suất
                prob = Rational(n_A, n_omega)

                # Bước 4: Tạo các phương án sai (không trùng phương án đúng)
                da = "$%s$" % (latex(prob))

                wrong_answers = set()
                while len(wrong_answers) < 3:
                    mistakes = [
                        Rational(n_remain * 2, n_omega),
                        Rational(2 * 2, n_omega),
                        Rational(n_A, n_elements * (n_elements - 1)),
                        Rational(1, randint(10, 30)),
                        Rational(2, randint(5, 15))
                    ]
                    w = random.choice(mistakes)
                    w_str = "$%s$" % (latex(w))
                    if w_str != da:
                        wrong_answers.add(w_str)

                list_wrong = list(wrong_answers)

                # Câu hỏi
                noidungcauhoi = (
                    "Cho các chữ số $%s$. Gọi $M$ là tập hợp tất cả các số tự nhiên gồm 3 chữ số khác nhau lập từ các chữ số đã cho. "
                    "Lấy ngẫu nhiên một số thuộc $M$. Xác suất lấy được số có chứa hai chữ số $%s, %s$ và đồng thời chúng đứng cạnh nhau bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm)."
                    % (all_digits_str, latex(d1), latex(d2))
                )

                # Các đáp án
                da_d = "\\True " + da
                da_s1 = list_wrong[0]
                da_s2 = list_wrong[1]
                da_s3 = list_wrong[2]

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)


                h1=prob
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')

                # Nội dung lời giải chi tiết
                loigiai = (
                    "Số phần tử của tập hợp nguồn là $n = %s$. \\\\ "
                    "Số các số tự nhiên có 3 chữ số khác nhau lập từ các chữ số đã cho là $n(\\Omega) = A_{%s}^3 = %s$. \\\\ "
                    "Gọi $A$ là biến cố: \"Số được chọn có chứa hai chữ số $%s$ và $%s$ đứng cạnh nhau\". \\\\ "
                    "Để tạo ra số thỏa mãn biến cố $A$, ta thực hiện các bước sau: \\\\ "
                    "- Bước 1: Xếp hai chữ số $%s$ và $%s$ đứng cạnh nhau: Có $2! = 2$ cách hoán vị giữa chúng. \\\\ "
                    "- Bước 2: Chọn một chữ số còn lại từ $%s$ chữ số còn lại (loại $%s$ và $%s$): Có $%s$ cách chọn. \\\\ "
                    "- Bước 3: Coi cặp $\\{%s; %s\\}$ là một khối thống nhất. Ta hoán vị khối này với chữ số còn lại vừa chọn: Có $2! = 2$ cách xếp. \\\\ "
                    "Số kết quả thuận lợi cho biến cố $A$ là $n(A) = 2 \\cdot %s \\cdot 2 = %s$. \\\\ "
                    "Vậy xác suất cần tìm là $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = %s \\approx %s$."
                    % (
                        latex(n_elements), latex(n_elements), latex(n_omega),
                        latex(d1), latex(d2),
                        latex(d1), latex(d2),
                        latex(n_elements - 2), latex(d1), latex(d2), latex(n_remain),
                        latex(d1), latex(d2),
                        latex(n_remain), latex(n_A),
                        latex(n_A), latex(n_omega), latex(prob), kqz
                    )
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + str(dapan)+
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content 

