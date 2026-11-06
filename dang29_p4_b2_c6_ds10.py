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


def bt_dang29_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến thể
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random số liệu
                n11 = randint(5, 7)
                n12 = randint(2, 3) # Giảm nhẹ số hs lớp 12 để đảm bảo xác suất không quá nhỏ
                tong_hs = n11 + n12
                so_vach_ngan = n11 + 1 

                # Bước 1 & 2: Tính toán logic
                # Không gian mẫu: n!
                omega = factorial(tong_hs)

                # Biến cố A: Xếp n12 học sinh lớp 12 vào so_vach_ngan vị trí trống
                # Cách xếp n11 học sinh lớp 11: n11!
                xep_n11 = factorial(n11)

                # Cách chọn và xếp n12 học sinh lớp 12: A_n^k = n! / (n-k)!
                # Thay nP bằng công thức trực tiếp để tránh lỗi NameError
                xep_n12 = factorial(so_vach_ngan) / factorial(so_vach_ngan - n12)

                nA = xep_n11 * xep_n12
                xac_suat = Rational(nA, omega)

                # Bước 4: Tạo phương án nhiễu (không trùng đáp án đúng)
                da_dung = '$%s$' % (latex(xac_suat))

                s = []
                # Sai lầm 1: Dùng tổ hợp binomial(n, k) thay vì chỉnh hợp
                sai1 = Rational(xep_n11 * binomial(so_vach_ngan, n12), omega)
                # Sai lầm 2: Quên hoán vị học sinh lớp 11
                sai2 = Rational(xep_n12, omega)
                # Sai lầm 3: Nhầm số vị trí trống (chỉ tính kẽ hở ở giữa: n11-1)
                if n11 - 1 >= n12:
                    xep_n12_sai = factorial(n11 - 1) / factorial(n11 - 1 - n12)
                    sai3 = Rational(xep_n11 * xep_n12_sai, omega)
                else:
                    sai3 = Rational(1, tong_hs * 2)

                # Gom các đáp án sai, lọc trùng với đáp án đúng
                temp_s = [sai1, sai2, sai3, Rational(1, 12), Rational(5, 72), Rational(7, 12)]
                for i in temp_s:
                    val = '$%s$' % (latex(i))
                    if val != da_dung and val not in s:
                        s.append(val)

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Có $%s$ học sinh lớp 11 và $%s$ học sinh lớp 12 được xếp ngẫu nhiên vào $%s$ ghế thành một dãy. Tính xác suất để xếp được $%s$ học sinh lớp 12 xen kẽ giữa $%s$ học sinh lớp 11.'''
                                 % (latex(n11), latex(n12), latex(tong_hs), latex(n12), latex(n11)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Không gian mẫu là số cách sắp xếp tất cả $%s$ học sinh vào một ghế dài. \\\\
                             Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = %s!$. \\\\
                             Gọi $A$ là biến cố "Xếp $%s$ học sinh lớp 12 xen kẽ giữa $%s$ học sinh lớp 11". Ta mô tả khả năng thuận lợi của biến cố $A$ như sau: \\\\
                             + Đầu tiên xếp $%s$ học sinh lớp 11 thành một dãy, có $%s!$ cách. \\\\
                             + Sau đó xem $%s$ học sinh này như $%s$ vách ngăn nên có $%s$ vị trí để xếp $%s$ học sinh lớp 12 (gồm $%s$ vị trí giữa $%s$ học sinh và 2 vị trí hai đầu). Do đó có $A_{%s}^{%s}$ cách xếp $%s$ học sinh lớp 12. \\\\
                             Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = %s! \\cdot A_{%s}^{%s}$. \\\\
                             Vậy xác suất cần tính là $P\\left(A\\right) = \\frac{%s! \\cdot A_{%s}^{%s}}{%s!} = %s$.'''
                           % (latex(tong_hs), latex(tong_hs), 
                              latex(n12), latex(n11), 
                              latex(n11), latex(n11), 
                              latex(n11), latex(n11), latex(so_vach_ngan), latex(n12), 
                              latex(n11 - 1), latex(n11), latex(so_vach_ngan), latex(n12), latex(n12),
                              latex(n11), latex(so_vach_ngan), latex(n12),
                              latex(n11), latex(so_vach_ngan), latex(n12), latex(tong_hs), latex(xac_suat)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

