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


def bt_dang59_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 & B3: Nghiên cứu đề bài và Random các dữ kiện bài toán
                N = randint(100, 150)       # Tổng số vé
                n1 = randint(1, 3)          # Số vé giải nhất (1tr)
                n2 = randint(4, 8)          # Số vé giải nhì (500k)
                n3 = randint(10, 15)        # Số vé giải ba (100k)
                n0 = N - n1 - n2 - n3       # Số vé không trúng thưởng

                # Tính toán tổ hợp
                total_ways = math.comb(N, 3)

                # Biến cố đối: Trúng dưới 300.000đ (0đ, 100k, 200k)
                case_0 = math.comb(n0, 3)                           # 0đ: 3 vé hụt
                case_100 = math.comb(n3, 1) * math.comb(n0, 2)      # 100k: 1 giải ba, 2 hụt
                case_200 = math.comb(n3, 2) * math.comb(n0, 1)      # 200k: 2 giải ba, 1 hụt

                complement_ways = case_0 + case_100 + case_200
                prob_A = (total_ways - complement_ways) / total_ways

                # B2: Viết lại kết quả dạng số thập phân làm tròn đến hàng phần chục (0.1)
                kq_dec = Decimal(str(prob_A)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',') # Định dạng dấu phẩy theo yêu cầu

                # Đáp án đúng
                da = '$%s$' % (kq_str)

                # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                # Tạo các phương án nhiễu quanh giá trị đúng
                val = float(kq_dec)
                s_raw = [
                    round(val + 0.1, 1),
                    round(val + 0.2, 1),
                    round(val - 0.1, 1),
                    round(val - 0.2, 1),
                    round(val + 0.3, 1)
                ]

                s_unique = []
                for item in s_raw:
                    item_str = str(item).replace('.', ',')
                    if item_str != kq_str and item >= 0 and item_str not in s_unique:
                        s_unique.append('$%s$' % item_str)

                # Chọn 3 đáp án sai
                random.shuffle(s_unique)
                das1, das2, das3 = s_unique[:3]

                # Câu hỏi
                noidungcauhoi = ('''Một hộp có $%s$ vé xổ số, trong đó có $%s$ vé trúng giải nhất (mỗi vé $1.000.000$ đồng), $%s$ vé trúng giải nhì (mỗi vé $500.000$ đồng), $%s$ vé trúng giải ba (mỗi vé $100.000$ đồng), các vé còn lại không trúng thưởng. Xác suất để một người mua ngẫu nhiên $3$ vé và trúng được ít nhất $300.000$ đồng bằng bao nhiêu? (làm tròn đến hàng phần trăm).'''
                                 % (latex(N), latex(n1), latex(n2), latex(n3)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Số vé không trúng thưởng là $%s - (%s + %s + %s) = %s$ vé.\\\\
                           Số phần tử của không gian mẫu là $n(\\Omega) = C_{%s}^3 = %s$.\\\\
                           Gọi $A$ là biến cố: "Người đó trúng được ít nhất $300.000$ đồng".\\\\
                           Khi đó $\\overline{A}$ là biến cố: "Người đó trúng được dưới $300.000$ đồng".\\\\
                           Để tổng tiền nhận được dưới $300.000$ đồng, người đó chỉ có thể rơi vào các trường hợp:\\\\
                           - TH1: Chọn $3$ vé không trúng thưởng: $C_{%s}^3 = %s$ cách.\\\\
                           - TH2: Chọn $1$ vé giải ba và $2$ vé không trúng: $C_{%s}^1 \\cdot C_{%s}^2 = %s$ cách.\\\\
                           - TH3: Chọn $2$ vé giải ba và $1$ vé không trúng: $C_{%s}^2 \\cdot C_{%s}^1 = %s$ cách.\\\\
                           Số kết quả thuận lợi cho biến cố đối là $n(\\overline{A}) = %s + %s + %s = %s$.\\\\
                           Xác suất của biến cố $A$ là $P(A) = 1 - \\frac{n(\\overline{A})}{n(\\Omega)} = 1 - \\frac{%s}{%s} \\approx %s$.'''

                           % (latex(N), latex(n1), latex(n2), latex(n3), latex(n0),
                              latex(N), latex(total_ways),
                              latex(n0), latex(case_0),
                              latex(n3), latex(n0), latex(case_100),
                              latex(n3), latex(n0), latex(case_200),
                              latex(case_0), latex(case_100), latex(case_200), latex(complement_ways),
                              latex(complement_ways), latex(total_ways), kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

