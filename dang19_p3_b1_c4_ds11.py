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


def bt_dang19_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                start_idx = randint(2, 5) 


                tu_so_kq = start_idx - 1
                mau_so_kq = start_idx
                ket_qua_dung = Rational(tu_so_kq, mau_so_kq)
                h1=ket_qua_dung
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kq).replace('.', ',')

                # --- BƯỚC 3: TẠO CÁC ĐÁP ÁN TRẮC NGHIỆM (DISTRACTORS) ---
                # Tạo đáp án đúng
                da_dung_latex = '$' + latex(ket_qua_dung) + '$'

                # Tạo đáp án sai (Nhiễu)
                # Nhiễu 1: Nghịch đảo kết quả
                da_sai1 = Rational(mau_so_kq, tu_so_kq)
                # Nhiễu 2: Cộng thêm 1 vào tử (hoặc sai lệch nhỏ)
                da_sai2 = Rational(tu_so_kq + 1, mau_so_kq + 1)
                # Nhiễu 3: Số nguyên hoặc 1 hoặc 0
                da_sai3 = 1

                # Danh sách đáp án dạng chuỗi
                ds_dapan = [da_dung_latex]

                # Thêm nhiễu và kiểm tra trùng lặp (cơ bản)
                if da_sai1 != ket_qua_dung:
                    ds_dapan.append('$' + latex(da_sai1) + '$')
                else:
                     ds_dapan.append('$' + latex(ket_qua_dung + S(1)/2) + '$')

                if da_sai2 != ket_qua_dung and da_sai2 != da_sai1:
                    ds_dapan.append('$' + latex(da_sai2) + '$')
                else:
                    ds_dapan.append('$' + latex(ket_qua_dung - S(1)/3) + '$')

                if da_sai3 != ket_qua_dung:
                    ds_dapan.append('$' + latex(da_sai3) + '$')
                else:
                    ds_dapan.append('$0$')

                # Đảm bảo đủ 4 đáp án (nếu logic trên bị trùng nhiều)
                while len(ds_dapan) < 4:
                    r = random.choice([2, 3, 4, 5])
                    val = Rational(1, r)
                    s_val = '$' + latex(val) + '$'
                    if s_val not in ds_dapan:
                        ds_dapan.append(s_val)

                # Trộn đáp án
                da_d = '\\True ' + ds_dapan[0]
                list_mix = [da_d] + ds_dapan[1:4]
                random.shuffle(list_mix)

                # --- BƯỚC 4: TẠO NỘI DUNG CÂU HỎI (Latex) ---
                # Xây dựng chuỗi hiển thị đề bài
                term_1 = latex(start_idx)
                term_2 = latex(start_idx + 1)

                noidungcauhoi = ('Giới hạn $\\lim_{n \\to +\\infty} \\left[ \\left(1-\\frac{1}{%s^2}\\right)\\left(1-\\frac{1}{%s^2}\\right)...\\left(1-\\frac{1}{n^2}\\right) \\right]$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                    % (term_1, term_2)
                )

                # --- BƯỚC 5: TẠO LỜI GIẢI CHI TIẾT (Tự động theo start_idx) ---
                # Tính toán các giá trị mẫu cho lời giải
                # u_start
                u1_num = start_idx**2 - 1
                u1_den = start_idx**2
                u1_latex = latex(Rational(u1_num, u1_den))
                u1_phantich = r'\frac{%s \cdot %s}{%s \cdot %s}' % (start_idx-1, start_idx+1, start_idx, start_idx)

                # u_start+1
                idx2 = start_idx + 1
                u2_num = idx2**2 - 1
                u2_den = idx2**2
                u2_latex = latex(Rational(u2_num, u2_den))
                u2_phantich = r'\frac{%s \cdot %s}{%s \cdot %s}' % (idx2-1, idx2+1, idx2, idx2)

                # Công thức rút gọn cuối cùng
                # Quy luật: ((m-1)/m) * ((n+1)/n)
                term_dau = r'\frac{%s}{%s}' % (start_idx-1, start_idx)
                term_cuoi = r'\frac{n+1}{n}'

                loigiai = ('''Xét dãy số $(u_n)$, với $u_n = \\left(1-\\frac{1}{%s^2}\\right)\\left(1-\\frac{1}{%s^2}\\right)...\\left(1-\\frac{1}{n^2}\\right)$, $n \\ge %s, n \\in \\mathbb{N}$. \\\\
                Ta có: \\\\
                $u_{%s} = 1 - \\frac{1}{%s^2} = %s = %s$; \\\\
                $u_{%s} = \\left(1-\\frac{1}{%s^2}\\right)\\left(1-\\frac{1}{%s^2}\\right) = %s \\cdot %s = %s \\cdot %s$; \\\\
                ...... \\\\
                $u_n = %s \\cdot %s$. \\\\
                Khi đó $\\lim_{n \\to +\\infty} \\left[ \\left(1-\\frac{1}{%s^2}\\right)...\\left(1-\\frac{1}{n^2}\\right) \\right] = \\lim_{n \\to +\\infty} \\frac{%s(n+1)}{%sn} = %s \\approx %s$.'''
                % (
                    term_1, term_2, term_1, # Dòng 1
                    term_1, term_1, u1_latex, u1_phantich, # Dòng u_start
                    term_2, term_1, term_2, u1_latex, u2_latex, u1_phantich, u2_phantich, # Dòng u_start+1
                    term_dau, term_cuoi, # Dòng u_n
                    term_1, # Dòng Khi đó...
                    start_idx-1, start_idx, # Dòng kết quả rút gọn
                    latex(ket_qua_dung),str(kq1) # Kết quả cuối
                ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

