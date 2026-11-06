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


def bt_dang10_p1_b1_c3_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Dict lưu trữ các hàng quy tròn và vị trí tương ứng để làm tròn
                dict_hang = {-1: 'hàng chục', -2: 'hàng trăm', -3: 'hàng nghìn', -4: 'hàng chục nghìn', -5: 'hàng trăm nghìn'}

                # Bốc ngẫu nhiên một hàng để quy tròn
                p = random.choice(list(dict_hang.keys()))
                ten_hang = dict_hang[p]

                # Tạo ngẫu nhiên một số có 7-8 chữ số
                N = random.randint(10000000, 99999999)

                # Tính kết quả đúng
                kq_dung = round(N, p)

                # --- XÂY DỰNG CÁC ĐÁP ÁN NHIỄU (SAI) ---
                s_vals = set()

                # 1. Sai do làm tròn sai vị trí hàng (lệch 1 hàng)
                s_vals.add(round(N, p + 1) if p < -1 else round(N, p - 1))
                s_vals.add(round(N, p - 1))

                # 2. Sai do nhầm lẫn giữ nguyên số ban đầu
                s_vals.add(N)

                # 3. Sai do làm tròn ngược quy tắc (nhỏ hơn 5 lại cộng thêm, hoặc >=5 lại giữ nguyên)
                if kq_dung > N:
                    s_vals.add(kq_dung - 10**abs(p))
                elif kq_dung < N:
                    s_vals.add(kq_dung + 10**abs(p))

                # Loại bỏ đáp án đúng ra khỏi tập đáp án nhiễu
                if kq_dung in s_vals:
                    s_vals.remove(kq_dung)

                # Chuyển set về list và bổ sung thêm nếu chưa đủ 3 đáp án nhiễu
                s_vals = list(s_vals)
                while len(s_vals) < 3:
                    fake_val = kq_dung + random.choice([-1, 1]) * random.randint(1, 5) * 10**abs(p)
                    if fake_val != kq_dung and fake_val not in s_vals:
                        s_vals.append(fake_val)

                random.shuffle(s_vals)

                # Câu hỏi
                noidungcauhoi = ('''Số quy tròn của $%s$ đến %s là''' % (latex(N), ten_hang))

                # Các đáp án
                da = '$%s$' % (latex(kq_dung))
                das1 = '$%s$' % (latex(s_vals[0]))
                das2 = '$%s$' % (latex(s_vals[1]))
                das3 = '$%s$' % (latex(s_vals[2]))

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                chuso_xet = (N // 10**(abs(p)-1)) % 10
                giai_thich = "lớn hơn hoặc bằng $5$ nên ta cộng thêm $1$ vào hàng quy tròn" if chuso_xet >= 5 else "nhỏ hơn $5$ nên ta giữ nguyên chữ số hàng quy tròn"

                loigiai = ('''Theo quy tắc quy tròn số, chữ số ngay sau %s là $%s$, %s và đổi các chữ số sau nó thành số $0$. \\\\
                              Vậy số quy tròn của $%s$ là $%s$.''' 
                           % (ten_hang, latex(chuso_xet), giai_thich, latex(N), latex(kq_dung)))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

