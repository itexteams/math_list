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


def bt_dang20_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Chọn một số thực từ 1.0 đến 5.0, bước nhảy 0.1
            dan_so_dau_trieu = random.choice([round(i / 10, 1) for i in range(10, 51)])
            u1_nghin = int(dan_so_dau_trieu * 1000)

            # Mức tăng dân số mỗi năm (nghìn người) -> d (công sai)
            d = random.choice(list(range(10, 55, 5)))

            # Năm bắt đầu (Y_start)
            nam_bat_dau = random.choice(list(range(2015, 2024)))

            # Khoảng thời gian (số năm tăng trưởng n-1)
            so_nam_tang = random.choice(list(range(8, 16)))

            # Năm cần tìm (Y_end)
            nam_can_tim = nam_bat_dau + so_nam_tang

            # --- 2. Tính toán kết quả ---
            n = so_nam_tang + 1 # Số hạng cần tìm
            u_n = u1_nghin + so_nam_tang * d # Dân số năm cần tìm (nghìn người)

            # --- 3. Định dạng đáp án trắc nghiệm ---

            # Đáp án đúng (kết quả)
            da = '$%s$ (nghìn người)' % (latex(u_n))
            da_d = ('\\True ' + str(da))

            # Các đáp án sai: Sử dụng list để đảm bảo các đáp án sai khác nhau
            sai_so_list = [d, -d, 2*d, -2*d, 3*d]
            random.shuffle(sai_so_list)

            # Tạo 3 đáp án sai khác nhau
            das1 = '$%s$ (nghìn người)' % (latex(u_n + sai_so_list[0]))
            das2 = '$%s$ (nghìn người)' % (latex(u_n + sai_so_list[1]))
            das3 = '$%s$ (nghìn người)' % (latex(u_n + sai_so_list[2]))

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1) 

            # --- 4. Nội dung Câu hỏi và Lời giải ---

            # Biểu diễn dân số ban đầu dưới dạng phân số/số thập phân cho LaTeX (Đã sửa lỗi NameError)
            dan_so_latex = latex(Rational(str(dan_so_dau_trieu)).limit_denominator(10)).replace('.', ',')

            # Câu hỏi
            noidungcauhoi = (
                '''Vào năm $%s$, dân số của một thành phố là khoảng $%s$ triệu người. Giả sử mỗi năm, dân số của thành phố này tăng thêm khoảng $%s$ nghìn người. Ước tính dân số của thành phố này vào năm $%s$ bằng bao nhiêu nghìn người?'''
                % (latex(nam_bat_dau), dan_so_latex, latex(d), latex(nam_can_tim))
            )

            # Lời giải (Đã sửa lỗi TypeError: thiếu đối số trong phần tính toán chi tiết)
            loigiai = (
                '''Dân số mỗi năm của thành phố lập thành cấp số cộng có số hạng đầu $u_1 = %s$, công sai $d = %s$ (nghìn người). \\\\
                Dân số mỗi năm có dạng tổng quát là: $u_k = u_1 + (k-1)d$. \\\\
                Năm $%s$ là năm thứ $n = %s - %s + 1 = %s$. \\\\
                Dân số ước tính vào năm $%s$ là: \\\\
                $u_{%s} = %s + (%s-1) \\cdot %s = %s + %s \\cdot %s = %s$ (nghìn người).'''
                % (latex(u1_nghin), latex(d), # 2 đối số
                   latex(nam_can_tim), latex(nam_can_tim), latex(nam_bat_dau), latex(n), # 4 đối số
                   latex(nam_can_tim), # 1 đối số
                   # 8 đối số sau (Tổng cộng: 2+4+1+8 = 15 đối số)
                   latex(n), latex(u1_nghin), latex(n), latex(d), latex(u1_nghin), latex(so_nam_tang), latex(d), latex(u_n) 
                  )
            )
                #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(u_n))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content 

