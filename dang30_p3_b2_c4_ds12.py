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


def bt_dang30_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Xác suất kinh tế tăng trưởng (p1) và suy thoái (p2)
                p1 = randint(5, 7) * 10 # Ví dụ: 50%, 60%, 70%
                p2 = 100 - p1

                # Kịch bản tăng trưởng: xác suất cổ phiếu (s1) và trái phiếu (b1) lãi cao
                s1 = randint(7, 9) * 10 # 70% - 90%
                b1 = randint(2, 4) * 10 # 20% - 40%

                # Kịch bản suy thoái: xác suất cổ phiếu (s2) và trái phiếu (b2) lãi cao
                s2 = randint(5, 15)      # 5% - 15%
                b2 = randint(6, 8) * 10 # 60% - 80%

                # Tính toán các giá trị xác suất (dưới dạng số thập phân)
                prob_A = p2 / 100 # Xác suất suy thoái
                prob_not_A = p1 / 100 # Xác suất tăng trưởng
                prob_B_given_A = b2 / 100 # Trái phiếu lãi cao khi suy thoái
                prob_B_given_not_A = b1 / 100 # Trái phiếu lãi cao khi tăng trưởng

                # P(AB) = Xác suất suy thoái và trái phiếu lãi cao
                p_ab = prob_A * prob_B_given_A

                # P(B) = Xác suất trái phiếu lãi cao (Công thức xác suất đầy đủ)
                p_b = (prob_not_A * prob_B_given_not_A) + (prob_A * prob_B_given_A)

                # P(A|B) = Xác suất suy thoái khi biết trái phiếu lãi cao (Bayes)
                kq_final = p_ab / p_b

                # Làm tròn kết quả đến hàng phần trăm
                kq_dec = Decimal(str(kq_final)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')

                # --- B4: Điều chỉnh các phương án sai ---
                da = '$%s$' % (kq_str)

                s = []
                # Tạo các đáp án nhiễu bằng cách cộng/trừ các giá trị nhỏ
                offsets = [0.08, -0.08, 0.12, -0.12, 0.15, -0.15, 0.05, -0.05]
                random.shuffle(offsets)
                for off in offsets:
                    val = float(kq_dec) + off
                    if 0.1 < val < 0.9:
                        val_str = str(Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        if val_str != kq_str:
                            s.append('$%s$' % val_str)

                # Chọn 3 đáp án sai từ danh sách
                s = list(set(s)) # Loại bỏ trùng lặp nếu có
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- B2: Viết lại đề bài và lời giải theo mẫu ---
                noidungcauhoi = (
                    'Một nhà đầu tư xem xét đầu tư vào hai loại tài sản: cổ phiếu và trái phiếu. Qua nghiên cứu thị trường có hai kịch bản sau có thể xảy ra:\n'
                    'Kinh bản kinh tế tăng trưởng: xác suất xảy ra kinh tế tăng trưởng trong năm tới là $%s$\\%%. Trong kịch bản này, xác suất cổ phiếu mang lại lợi nhuận cao là $%s$\\%% và xác suất trái phiếu mang lại lợi nhuận cao là $%s$\\%%.\n'
                    'Kinh bản kinh tế suy thoái: xác suất xảy ra kịch bản kinh tế suy thoái trong năm tới là $%s$\\%%. Trong kịch bản này, xác suất cổ phiếu mang lại lợi nhuận cao là $%s$\\%% và xác suất trái phiếu mang lại lợi nhuận cao là $%s$\\%%.\n'
                    'Vào cuối năm, nhà đầu tư nhận thấy rằng trái phiếu đã mang lại lợi nhuận cao. Xác suất để kịch bản kinh tế trong năm đó là suy thoái bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                    % (latex(p1), latex(s1), latex(b1), latex(p2), latex(s2), latex(b2))
                )

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Trình bày lời giải chi tiết
                p_ab_str = str(p_ab).replace('.', ',')
                p_b_str = str(round(p_b, 4)).replace('.', ',')

                loigiai = (
                    'Gọi $A$ là biến cố: "kịch bản kinh tế trong năm đó là suy thoái" \\\\\n'
                    'Gọi $B$ là biến cố: "trái phiếu đã mang lại lợi nhuận cao" \\\\\n'
                    'Xác suất kịch bản kinh tế suy thoái và trái phiếu đã mang lại lợi nhuận cao là: \\\\\n'
                    '$P(AB) = %s\\%% \\cdot %s\\%% = %s$ \\\\\n'
                    'Xác suất trái phiếu mang lại lợi nhuận cao (theo công thức xác suất đầy đủ) là: \\\\\n'
                    '$P(B) = %s\\%% \\cdot %s\\%% + %s\\%% \\cdot %s\\%% = %s$ \\\\\n'
                    'Xác suất để kịch bản kinh tế trong năm đó là suy thoái với điều kiện trái phiếu đã mang lại lợi nhuận cao là: \\\\\n'
                    '$P(A|B) = \\frac{P(AB)}{P(B)} = \\frac{%s}{%s} \\approx %s$.'
                    % (latex(p2), latex(b2), p_ab_str, 
                       latex(p1), latex(b1), latex(p2), latex(b2), p_b_str,
                       p_ab_str, p_b_str, kq_str)
                )
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

