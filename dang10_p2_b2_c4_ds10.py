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


def bt_dang10_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Hàm bổ trợ để chuyển dấu . thành , cho số thập phân
            def format_vn(value):
                return str(value).replace('.', ',')

            # Khai báo biến sympy
            x_sym = symbols('x')

            # --- BƯỚC 1: RANDOM DỮ LIỆU BÀI TOÁN ---
            gia_mua = random.randint(25, 30) 
            ln_bandau = random.randint(3, 6)
            gia_ban_cu = gia_mua + ln_bandau
            sl_cu = random.randint(400, 800)
            he_so_tang = random.choice([100, 150, 200, 250])

            A = -he_so_tang
            B = he_so_tang * ln_bandau - sl_cu
            C = ln_bandau * sl_cu

            # Tọa độ đỉnh parabol
            x_max = Rational(-B, 2*A)
            y_max = A*x_max**2 + B*x_max + C

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Một doanh nghiệp tư nhân $A$ chuyên kinh doanh xe gắn máy các loại. Hiện nay doanh nghiệp đang tập trung chiến lược vào kinh doanh xe Honda Future Fi với chi phí mua vào một chiếc là $%s$ triệu đồng và bán ra với giá là $%s$ triệu đồng. Với giá bán này thì số lượng xe mà khách hàng sẽ mua trong một năm là $%s$ chiếc. Nhằm mục tiêu đẩy mạnh hơn nữa lượng tiêu thụ dòng xe này, doanh nghiệp dự định giảm giá bán và ước tính rằng nếu giảm $1$ triệu đồng mỗi chiếc xe thì số lượng xe bán ra trong một năm sẽ tăng thêm $%s$ chiếc. Gọi $x$ (triệu đồng) là số tiền mà doanh nghiệp $A$ dự định giảm giá và $T$ là lợi nhuận mà doanh nghiệp thu được trong một năm.''' 
                             %(gia_mua, gia_ban_cu, sl_cu, he_so_tang))

            ########################################################################
            # Nhận biết
            nb_da_1_d = '\\True Lợi nhuận thu được khi bán một chiếc xe là $%s - x$ (triệu đồng)' % (ln_bandau)
            nb_da_1_s = 'Lợi nhuận thu được khi bán một chiếc xe là $%s - x$ (triệu đồng)' % (gia_ban_cu)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Lợi nhuận thu được khi bán một chiếc xe là $%s - x - %s = %s - x$ (triệu đồng).''' % (gia_ban_cu, gia_mua, ln_bandau))

            ########################################################################
            # Thông hiểu
            th_da_1_d = '\\True Số xe mà doanh nghiệp sẽ bán được trong một năm là $%s + %sx$' % (sl_cu, he_so_tang)
            th_da_1_s = 'Số xe mà doanh nghiệp sẽ bán được trong một năm là $%s + %sx$' % (gia_mua, he_so_tang)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Vì giảm $1$ triệu đồng thì tăng $%s$ xe, nên giảm $x$ triệu đồng thì số xe tăng thêm là $%sx$. Vậy tổng số xe bán được là $%s + %sx$.''' % (he_so_tang, he_so_tang, sl_cu, he_so_tang))

            ########################################################################
            # Vận dụng
            vd_da_1_d = '\\True Hàm số biểu diễn lợi nhuận $T$ theo $x$ là $T = %sx^2 + %sx + %s$' % (A, B, C)
            vd_da_1_s = 'Hàm số biểu diễn lợi nhuận $T$ theo $x$ là $T = %sx^2 - %sx + %s$' % (A, B, C)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Lợi nhuận thu được trong một năm là $T = (%s - x)(%s + %sx) = %sx^2 + %sx + %s$.''' % (ln_bandau, sl_cu, he_so_tang, A, B, C))

            ########################################################################
            # Vận dụng cao
            # Sử dụng format_vn cho các giá trị số thực
            gia_moi_max = format_vn(round(float(gia_ban_cu - x_max), 3))
            vdc_da_1_d = '\\True Để lợi nhuận cao nhất thì mức giá bán mới của chiếc xe nên là $%s$ triệu đồng' % (gia_moi_max)
            vdc_da_1_s = 'Để lợi nhuận cao nhất thì doanh nghiệp nên giảm giá $%s$ triệu đồng' % (ln_bandau)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Tính giá trị f(ln_bandau) và chuyển dấu phẩy
            f_tai_bien = format_vn(float(A*ln_bandau**2 + B*ln_bandau + C))

            loigiai_vdc_1 = ('''Xét hàm số $f(x) = %sx^2 + %sx + %s$ trên đoạn $[0; %s]$.\\\\
            Ta có bảng biến thiên:\\\\
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$f\'(x)$/0.7,$f(x)$/2.1}
            {$0$,$%s$,$%s$}
            \\tkzTabLine{,+,0,-,}
            \\tkzTabVar{-/$%s$,+/$%s$,-/$0$}
            \\end{tikzpicture} \\\\
            Dựa vào bảng biến thiên, lợi nhuận đạt cực đại khi $x = %s$. Khi đó giá bán mới là $%s - %s = %s$ triệu đồng.''' 
            %(A, B, C, ln_bandau, latex(x_max), ln_bandau, C, latex(y_max), latex(x_max), gia_ban_cu, latex(x_max), gia_moi_max))

            # --- BƯỚC 3: KIỂM TRA ĐIỀU KIỆN ĐÁP ÁN ĐÚNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # --- BƯỚC 4: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(ans_nb)+'}\n'
                '{'+str(ans_th)+'}\n'
                '{'+str(ans_vd)+'}\n'
                '{'+str(ans_vdc)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+')
            return content

