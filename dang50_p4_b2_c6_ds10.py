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


def bt_dang50_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # n_total: Tổng số sản phẩm (từ 10 đến 15)
                # n_phe: Số phế phẩm (từ 2 đến 3)
                # n_chon: Số sản phẩm chọn ra (từ 4 đến 6)
                n_total = randint(10, 15)
                n_phe = randint(2, 3)
                n_chon = randint(4, 6)

                # Đảm bảo số sản phẩm chọn ra không vượt quá số sản phẩm tốt
                n_tot = n_total - n_phe
                if n_chon > n_tot:
                    n_chon = n_tot

                # Tính toán các giá trị cho lời giải
                # n(Omega) = C(n_total, n_chon)
                omega = binomial(n_total, n_chon)
                # n(A) = C(n_tot, n_chon)
                thuan_loi = binomial(n_tot, n_chon)
                # Xác suất P(A)
                xac_suat = Rational(thuan_loi, omega)

                # Đáp án đúng
                da = "$%s$" % (latex(xac_suat))

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    # Tạo các phân số ngẫu nhiên hoặc biến tấu từ kết quả
                    tu = randint(1, 15)
                    mau = randint(tu + 1, 30)
                    gia_tri_sai = Rational(tu, mau)
                    da_sai = "$%s$" % (latex(gia_tri_sai))
                    if da_sai != da and da_sai not in s:
                        s.append(da_sai)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2: Viết lại y hệt đề bài theo mẫu)
                noidungcauhoi = ("Chọn ngẫu nhiên $%s$ sản phẩm trong $%s$ sản phẩm. Biết rằng trong $%s$ sản phẩm đó có $%s$ phế phẩm. Tính xác suất để trong $%s$ sản phẩm được chọn không có phế phẩm nào."
                                 %(latex(n_chon), latex(n_total), latex(n_total), latex(n_phe), latex(n_chon)))

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết chi tiết, không viết tắt, không dùng tiền tố r)
                loigiai = ("Gọi $A$ là biến cố: \"Trong $%s$ sản phẩm được chọn không có phế phẩm nào\". \\\\ "
                           "Số phần tử của không gian mẫu là: $n(\\Omega) = C_{%s}^{%s} = %s$. \\\\ "
                           "Số sản phẩm không bị lỗi (sản phẩm tốt) trong $%s$ sản phẩm là: $%s - %s = %s$ sản phẩm. \\\\ "
                           "Để chọn được $%s$ sản phẩm mà không có phế phẩm nào, ta phải chọn $%s$ sản phẩm từ $%s$ sản phẩm tốt đó. \\\\ "
                           "Số kết quả thuận lợi cho biến cố $A$ là: $n(A) = C_{%s}^{%s} = %s$. \\\\ "
                           "Xác suất cần tìm là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{C_{%s}^{%s}}{C_{%s}^{%s}} = \\frac{%s}{%s} = %s$."
                           %(latex(n_chon), latex(n_total), latex(n_chon), latex(omega), 
                             latex(n_total), latex(n_total), latex(n_phe), latex(n_tot),
                             latex(n_chon), latex(n_chon), latex(n_tot),
                             latex(n_tot), latex(n_chon), latex(thuan_loi),
                             latex(n_tot), latex(n_chon), latex(n_total), latex(n_chon),
                             latex(thuan_loi), latex(omega), latex(xac_suat)))

            # Xuất câu trắc nghiệm (Không dùng raw string r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

