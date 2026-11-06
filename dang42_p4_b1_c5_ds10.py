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


def bt_dang42_p4_b1_c5_ds10(self):
            # Khai báo biến
            # --- Khai báo biến và Random hóa ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # n_cau: số lượng câu hỏi trắc nghiệm (ví dụ từ 8 đến 12)
                n_cau = randint(8, 11) 
                # n_chon: số lựa chọn cho mỗi câu (ví dụ từ 3 đến 5)
                n_chon = randint(3, 4)

                # Tổng số phương án trả lời khác nhau có thể có: n_chon ^ n_cau
                tong_pa = n_chon**n_cau
                # Kết quả tối thiểu để có ít nhất 2 phiếu giống nhau (Nguyên lý Dirichlet)
                kq_dung = tong_pa + 1

                # Chuyển số sang chuỗi để trình bày (có thể xử lý thay dấu chấm bằng phẩy nếu là số thập phân)
                # Tuy nhiên bài này là số nguyên lớn
                da_dung_str = str(kq_dung)

                # Các đáp án trắc nghiệm đúng
                du = ['$%s$' % (da_dung_str)]
                da = random.choice(du)

                # Các đáp án gây nhiễu (sai)
                # Đảm bảo không trùng với đáp án đúng
                s = [
                    '$%s$' % (latex(tong_pa)),
                    '$%s$' % (latex(kq_dung + 1)),
                    '$%s$' % (latex(kq_dung - 2)),
                    '$%s$' % (latex(n_chon**n_cau - 100)),
                    '$%s$' % (latex(n_chon * n_cau * 1000)), # Một con số giả định khác
                    '$%s$' % (latex(n_chon**(n_cau-1) + 1)),
                ]

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # --- Câu hỏi ---
                noidungcauhoi = ('''Một phiếu điều tra về đề tự học của học sinh gồm $%s$ câu hỏi trắc nghiệm, mỗi câu có $%s$ lựa chọn để trả lời. Khi tiến hành điều tra, phiếu thu lại được coi là hợp lệ nếu người được hỏi trả lời đủ $%s$ câu hỏi, mỗi câu chỉ chọn một phương án. Tìm số phiếu hợp lệ để trong số đó luôn có ít nhất hai phiếu trả lời giống hệt nhau cả $%s$ câu hỏi.'''
                                 % (latex(n_cau), latex(n_chon), latex(n_cau), latex(n_cau)))

                # --- Các đáp án ---
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                loigiai = ('''Mỗi câu hỏi có $%s$ lựa chọn. \\\\
                             Suy ra $%s$ câu hỏi có $%s^{%s} = %s$ phương án trả lời khác nhau. \\\\
                             Theo nguyên lý Dirichlet, nếu có nhiều hơn $%s$ phiếu hợp lệ thì luôn có ít nhất hai phiếu trả lời giống hệt nhau. \\\\
                             Vậy số phiếu hợp lệ tối thiểu cần thiết là $%s + 1 = %s$ phiếu.'''
                           % (latex(n_chon), 
                              latex(n_cau), latex(n_chon), latex(n_cau), latex(tong_pa),
                              latex(tong_pa), 
                              latex(tong_pa), latex(kq_dung)))

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

