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


def bt_dang25_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Trong ảnh: m = 3, tổng đội = 9.
            m = random.choice([3, 4])  # Chọn mỗi bảng có 3 đội (tổng 9) hoặc 4 đội (tổng 12)
            n_vn = 3
            n_total = 3 * m
            n_foreign = n_total - n_vn

            # B2: Tính toán lời giải
            # 1. Không gian mẫu: Chia n_total đội vào 3 bảng A, B, C mỗi bảng m đội
            omega = binomial(n_total, m) * binomial(n_total - m, m) * binomial(m, m)

            # 2. Biến cố X: 3 đội VN ở 3 bảng khác nhau
            # Bước 1: Xếp 3 đội VN vào 3 bảng A, B, C: 3! cách
            cach_xep_vn = factorial(3)
            # Bước 2: Xếp n_foreign đội vào 3 bảng, mỗi bảng cần thêm (m-1) đội
            # Bảng A chọn m-1 đội từ n_foreign: C(n_foreign, m-1)
            # Bảng B chọn m-1 đội từ số còn lại: C(n_foreign - (m-1), m-1)
            # Bảng C chọn số còn lại: C(m-1, m-1)
            cach_xep_foreign = binomial(n_foreign, m - 1) * binomial(n_foreign - (m - 1), m - 1)

            omega_x = cach_xep_vn * cach_xep_foreign
            xac_suat = Rational(omega_x, omega)

            # B4: Điều chỉnh các phương án sai
            da_dung = "$%s$" % (latex(xac_suat))

            # Tạo danh sách các phương án sai không trùng lặp
            phuong_an_sai = set()
            while len(phuong_an_sai) < 3:
                # Sai lầm 1: Biến cố đối
                sai1 = "$%s$" % (latex(1 - xac_suat))
                # Sai lầm 2: Quên hoán vị 3! ở tử số
                sai2 = "$%s$" % (latex(Rational(omega_x // 6, omega)))
                # Sai lầm 3: Sai số ở mẫu số hoặc tử số ngẫu nhiên
                sai3 = "$%s$" % (latex(Rational(random.randint(1, 10), random.randint(20, 60))))

                for s in [sai1, sai2, sai3]:
                    if s != da_dung and len(phuong_an_sai) < 3:
                        phuong_an_sai.add(s)

            list_sai = list(phuong_an_sai)
            da_s1, da_s2, da_s3 = list_sai[0], list_sai[1], list_sai[2]

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Giải bóng chuyền VTV Cup gồm $%s$ đội bóng tham dự, trong đó có $%s$ đội nước ngoài và $%s$ đội của Việt Nam. "
                "Ban tổ chức cho bốc thăm ngẫu nhiên để chia thành 3 bảng $A, B, C$ và mỗi bảng có $%s$ đội. "
                "Xác suất để 3 đội bóng của Việt Nam ở 3 bảng khác nhau bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm)."
                % (latex(n_total), latex(n_foreign), latex(n_vn), latex(m))
            )
            h1=xac_suat
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.', ',')
            # Nội dung lời giải chi tiết
            loigiai = (
                "Không gian mẫu là số cách chia tùy ý $%s$ đội thành 3 bảng $A, B, C$, mỗi bảng $%s$ đội. \\\\ "
                "Suy ra số phần tử của không gian mẫu là $n(\\Omega) = C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s} = %s$. \\\\ "
                "Gọi $X$ là biến cố “3 đội bóng của Việt Nam ở 3 bảng khác nhau”. \\\\ "
                "Bước 1: Xếp 3 đội của Việt Nam vào 3 bảng khác nhau có $3! = %s$ cách. \\\\ "
                "Bước 2: Xếp $%s$ đội còn lại vào 3 bảng $A, B, C$, mỗi bảng cần thêm $%s$ đội, có $C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s} = %s$ cách. \\\\ "
                "Suy ra số phần tử của biến cố $X$ là: $|n(X)| = 3! \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s} = %s$. \\\\ "
                "Vậy xác suất cần tìm là: $P\\left( X \\right) = \\frac{%s}{%s} = %s \\approx %s$."
                % (
                    latex(n_total), latex(m), 
                    latex(n_total), latex(m), latex(n_total - m), latex(m), latex(m), latex(m), latex(omega),
                    latex(factorial(3)),
                    latex(n_foreign), latex(m - 1),
                    latex(n_foreign), latex(m - 1), latex(n_foreign - (m - 1)), latex(m - 1), latex(m - 1), latex(m - 1), latex(cach_xep_foreign),
                    latex(n_foreign), latex(m - 1), latex(n_foreign - (m - 1)), latex(m - 1), latex(m - 1), latex(m - 1), latex(omega_x),
                    latex(omega_x), latex(omega), latex(xac_suat),kqz
                )
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Trộn đáp án
            da_d = "\\True " + da_dung
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo mẫu
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + str(dapan)+
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content 

