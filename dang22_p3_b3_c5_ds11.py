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


def bt_dang22_p3_b3_c5_ds11(self):
            # Khai báo biến
            # --- Bước 1 & 3: Nghiên cứu đề bài và Thiết lập Random ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Số tiền gửi ban đầu (triệu đồng): chọn từ 100 đến 500, bước nhảy 50
                tien_gui = random.choice([100, 150, 200, 250, 300, 400, 500])

                # Kì hạn gốc (tháng)
                ki_han_goc = 12

                # Thời điểm muốn rút tiền (tháng): sau khi gửi được 7, 8 hoặc 9 tháng
                thoi_gian_da_gui = random.choice([7, 8, 9])
                thoi_gian_con_lai = ki_han_goc - thoi_gian_da_gui

                # Lãi suất kì hạn r (%)
                r_co_dinh = random.choice([0.6, 0.65, 0.7, 0.75])

                # Lãi suất không kì hạn (%)
                r_khong_ki_han = random.choice([0.01, 0.02, 0.03])

                # Lãi suất vay thế chấp (%) - thường cao hơn lãi suất gửi một chút
                r_vay = round(r_co_dinh + 0.05, 2)

                # --- Tính toán theo công thức lãi kép ---
                # 1. Số tiền lãi nếu gửi đúng kì hạn (L1)
                L1 = tien_gui * ((1 + r_co_dinh/100)**ki_han_goc) - tien_gui

                # 2. Số tiền phải trả cho ngân hàng nếu vay trong thời gian còn lại (N)
                N = tien_gui * ((1 + r_vay/100)**thoi_gian_con_lai) - tien_gui

                # 3. Số tiền lãi nếu rút sớm (L2) - hưởng lãi không kì hạn
                L2 = tien_gui * ((1 + r_khong_ki_han/100)**thoi_gian_da_gui) - tien_gui

                # 4. Số tiền đỡ thiệt (kq_chinh_xac)
                # Công thức: (Lãi nhận đủ - Lãi vay) - Lãi rút sớm
                kq_chinh_xac = (L1 - N) - L2

                # Làm tròn đến 3 chữ số thập phân để tính toán, sau đó làm tròn 1 chữ số cho đáp án
                kq_final = Decimal(float(kq_chinh_xac)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                da_dung_str = str(kq_final).replace('.', ',')

                # --- Bước 4: Tạo các phương án sai (không trùng đáp án đúng) ---
                sai_lech = [-1.5, -0.8, 1.2, 2.5, -3.2, 4.1]
                s = []
                while len(s) < 3:
                    val = kq_final + Decimal(str(random.choice(sai_lech)))
                    val_str = str(val.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if val_str != da_dung_str and val_str not in s:
                        s.append('$%s$' % val_str)

                da_d = '\\True $%s$' % da_dung_str
                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

                # --- Bước 2: Viết lại nội dung đề bài và lời giải ---
                noidungcauhoi = ('''Anh Bình gửi $%s$ triệu vào ngân hàng VB với kì hạn cố định $%s$ tháng và hưởng lãi suất $%s\\%%$/ tháng. Tuy nhiên sau khi gửi được tròn $%s$ tháng anh phải dùng đến $%s$ triệu trên. Anh đến ngân hàng định rút tiền thì được nhân viên ngân hàng tư vấn: “Nếu rút tiền trước kì hạn, toàn bộ số tiền anh gửi chỉ có lãi suất không kì hạn là $%s\\%%$/ tháng. Anh nên thế chấp sổ tiết kiệm đó tại ngân hàng để vay ngân hàng $%s$ triệu với lãi suất $%s\\%%$/ tháng. Khi sổ của anh đến kì hạn, anh có thể rút tiền để trả nợ ngân hàng”. Nếu làm theo tư vấn của nhân viên ngân hàng anh Bình sẽ đỡ thiệt một số tiền gần nhất với con số nào dưới đây (biết ngân hàng tính lãi theo thể thức lãi kép, kết quả làm tròn đến hàng phần chục).'''
                                 % (latex(tien_gui), latex(ki_han_goc), latex(r_co_dinh), 
                                    latex(thoi_gian_da_gui), latex(tien_gui), latex(r_khong_ki_han), 
                                    latex(tien_gui), latex(r_vay)))

                loigiai = ('''Số tiền lãi nhận được nếu anh Bình gửi đúng kì hạn là:
                             $L_1 = %s \\cdot (1 + %s\\%%)^{%s} - %s \\approx %s$ (triệu). \\\\
                             Số tiền lãi phải trả cho ngân hàng nếu vay $%s$ triệu trong $%s$ tháng còn lại là:
                             $N = %s \\cdot (1 + %s\\%%)^{%s} - %s \\approx %s$ (triệu). \\\\
                             Số tiền lãi nhận được nếu anh Bình rút tiền sau $%s$ tháng (lãi không kì hạn):
                             $L_2 = %s \\cdot (1 + %s\\%%)^{%s} - %s \\approx %s$ (triệu). \\\\
                             Số tiền anh Bình đỡ thiệt nếu làm theo tư vấn là:
                             $(L_1 - N) - L_2 = (%s - %s) - %s \\approx %s$ (triệu).'''
                           % (latex(tien_gui), latex(r_co_dinh), latex(ki_han_goc), latex(tien_gui), latex(round(L1, 5)),
                              latex(tien_gui), latex(thoi_gian_con_lai), latex(tien_gui), latex(r_vay), latex(thoi_gian_con_lai), latex(tien_gui), latex(round(N, 5)),
                              latex(thoi_gian_da_gui), latex(tien_gui), latex(r_khong_ki_han), latex(thoi_gian_da_gui), latex(tien_gui), latex(round(L2, 5)),
                              latex(round(L1, 5)), latex(round(N, 5)), latex(round(L2, 5)), latex(da_dung_str)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(da_dung_str))

            # Xuất kết quả theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

