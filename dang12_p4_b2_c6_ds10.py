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


def bt_dang12_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Thay đổi số mặt của con xúc xắc (thường là 6, có thể là 4, 8, 10, 12)
                # Ở đây chọn ngẫu nhiên số mặt n để bài toán đa dạng
                n = random.choice([6, 8, 10]) 
                so_cham = random.randint(1, n) # Mặt xuất hiện (ví dụ mặt 6 chấm)

                # Tính toán
                khong_gian_mau = n * n
                bien_co_doi = (n - 1) * (n - 1)
                so_phan_tu_A = khong_gian_mau - bien_co_doi

                # Đáp án đúng dưới dạng phân số tối giản hoặc giữ nguyên mẫu số n^2 như ảnh
                # Trong ảnh mẫu số giữ nguyên là 36 (6*6), nên ta sẽ giữ nguyên mẫu số n^2
                kq_tu = so_phan_tu_A
                kq_mau = khong_gian_mau

                da_dung = "$\\frac{%s}{%s}$" % (latex(kq_tu), latex(kq_mau))

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    sai_tu = random.randint(1, kq_mau - 1)
                    if sai_tu != kq_tu:
                        da_sai = "$\\frac{%s}{%s}$" % (latex(sai_tu), latex(kq_mau))
                        if da_sai not in s:
                            s.append(da_sai)

                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                # Thay thế dấu ngoặc ( ) bằng \left( \right) theo yêu cầu
                noidungcauhoi = ("Gieo một con xúc xắc $%s$ mặt hai lần. Tính xác suất để ít nhất một lần xuất hiện mặt $%s$ chấm."
                                 % (latex(n), latex(so_cham)))

                # Các đáp án
                da_d = ("\\True " + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2 - Viết lại y hệt bài toán)
                # Lưu ý: Không dùng tiền tố r, thay ( ) bằng \left( \right)
                loigiai = ("Số phần tử của không gian mẫu là $|\\Omega| = %s \\cdot %s = %s$. \\\\ "
                           "Gọi $A$ là biến cố 'Ít nhất một lần xuất hiện mặt %s chấm'. Để tìm số phần tử của biến cố $A$, "
                           "ta đi tìm số phần tử của biến cố đối $\\overline{A}$ là 'Không xuất hiện mặt %s chấm' \\\\ "
                           "$\\rightarrow |\\Omega_{\\overline{A}}| = %s \\cdot %s = %s \\rightarrow |\\Omega_A| = %s - %s = %s$. \\\\ "
                           "Vậy xác suất cần tính $P\\left( A \\right) = \\frac{%s}{%s}$."
                           % (latex(n), latex(n), latex(khong_gian_mau), 
                              latex(so_cham), latex(so_cham),
                              latex(n-1), latex(n-1), latex(bien_co_doi),
                              latex(khong_gian_mau), latex(bien_co_doi), latex(so_phan_tu_A),
                              latex(kq_tu), latex(kq_mau)))

            # Xuất câu trắc nghiệm
            content = ("\\begin{minipage}{\\textwidth} \n"
                       "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                       "\\loigiai{" + str(loigiai) + "}\n"
                       "\\end{ex}\n \\end{minipage} \n\n")
            return content 

