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


def bt_dang14_p1_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1 & B3: Nghiên cứu và thiết lập random
                # n_cau: Tổng số câu hỏi (ví dụ từ 40 đến 60)
                # k_dung: Số câu trả lời đúng (ngẫu nhiên để tạo ra số điểm tương ứng)
                n_cau = randint(40, 60)
                k_dung = randint(20, n_cau - 10)
                n_sai = n_cau - k_dung

                diem_moi_cau = 0.2
                # Tính tổng điểm, định dạng dùng dấu phẩy cho số thập phân
                tong_diem_val = round(k_dung * diem_moi_cau, 1)
                if tong_diem_val == int(tong_diem_val):
                    tong_diem = str(int(tong_diem_val))
                else:
                    tong_diem = str(tong_diem_val).replace('.', ',')

                # Xác suất thành công p=0,25 và thất bại q=0,75
                p_str = "0,25"
                q_str = "0,75"

                # B2: Viết lại bài toán và lời giải theo mẫu
                # Đáp án đúng (A)
                da_text = "0,25^{" + str(k_dung) + "} \\cdot 0,75^{" + str(n_sai) + "} \\cdot C_{" + str(n_cau) + "}^{" + str(n_sai) + "}"

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s_list = [
                    "1 - 0,25^{" + str(n_sai) + "} \\cdot 0,75^{" + str(k_dung) + "}", # Giống phương án B
                    "0,25^{" + str(n_sai) + "} \\cdot 0,75^{" + str(k_dung) + "}",      # Giống phương án C
                    "0,25^{" + str(k_dung) + "} \\cdot 0,75^{" + str(n_sai) + "}",      # Giống phương án D
                    "0,25^{" + str(k_dung) + "} \\cdot 0,75^{" + str(n_sai) + "} \\cdot C_{" + str(n_cau) + "}^{" + str(k_dung-1) + "}"
                ]

                # Lọc để đảm bảo không trùng đáp án đúng
                s_list = [item for item in s_list if item != da_text]
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ("Một đề thi trắc nghiệm gồm $" + str(n_cau) + "$ câu, mỗi câu có $4$ phương án trả lời trong đó chỉ có một phương án đúng, mỗi câu trả lời đúng được $0,2$ điểm. Một thí sinh làm bài bằng cách chọn ngẫu nhiên 1 trong 4 phương án ở mỗi câu. Xác suất để thí sinh đó được $" + tong_diem + "$ điểm là")

                # Các đáp án
                da_d = "\\True $" + da_text + "$"
                da_s1 = "$" + das1 + "$"
                da_s2 = "$" + das2 + "$"
                da_s3 = "$" + das3 + "$"

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ("Khi chọn ngẫu nhiên 1 trong 4 đáp án, xác suất trả lời đúng là 0,25 và xác suất trả lời sai là 0,75. \\\\ "
                           "Để được " + tong_diem + " điểm, thí sinh cần trả lời đúng " + str(k_dung) + " câu và sai " + str(n_sai) + " câu. \\\\ "
                           "Chọn " + str(n_sai) + " câu trong " + str(n_cau) + " câu để trả lời sai, có $C_{" + str(n_cau) + "}^{" + str(n_sai) + "}$ cách. \\\\ "
                           "Theo quy tắc nhân xác suất, ta có xác suất cần tính là: $P = " + da_text + "$.")

            # Xuất câu trắc nghiệm (không dùng raw string r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

