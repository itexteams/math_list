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


def bt_dang24_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Hàm hỗ trợ đổi dấu chấm thành dấu phẩy cho số thực và latex
            def format_vn(val):
                return str(val).replace('.', ',')

            def latex_vn(expr):
                return latex(expr).replace('.', ',')

            # --- BƯỚC 1: RANDOM DỮ LIỆU ---
            p_goc = 150
            m_goc = 20
            n_goc = 4000

            # Doanh thu thực tế: 150k = 0.15 triệu
            p_trieu = p_goc / 1000 

            noidungcauhoi = ('''Bộ phận sản xuất của một công ty xác định chi phí để sản xuất $x$ sản phẩm được cho bởi biểu thức $T(x) = x^2 + %s x + %s$ (triệu đồng). Giả sử $x$ sản phẩm đều được bán hết và giá bán mỗi sản phẩm là %s nghìn đồng. Bộ phận kinh doanh ước tính lợi nhuận khi bán $x$ sản phẩm được biểu thị theo hàm số bậc hai $f(x) = ax^2 + bx + c$.''' 
                             %(m_goc, n_goc, p_goc))

            ########################################################################
            # a) Doanh thu
            doanh_thu_sai = p_goc
            doanh_thu_dung = p_trieu

            da_a_d = '\\True Doanh thu khi bán được $x$ sản phẩm là $%s x$ (triệu đồng)' % (format_vn(doanh_thu_dung))
            da_a_s = 'Doanh thu khi bán được $x$ sản phẩm là $%s x$ (triệu đồng)' % (format_vn(doanh_thu_sai))
            list_da_a = [da_a_d, da_a_s]
            shuffled_a = random.choice(list_da_a)

            loigiai_a = ('''Đổi $%s$ nghìn đồng $= %s$ triệu đồng. Doanh thu khi bán $x$ sản phẩm là $R(x) = %s x$ (triệu đồng).''' 
                        % (p_goc, format_vn(doanh_thu_dung), format_vn(doanh_thu_dung)))

            ########################################################################
            # b) Hệ số a+b-c
            a_f = -1
            b_f = p_trieu - m_goc # 0.15 - 20 = -19.85
            c_f = -n_goc          # -4000
            tong = a_f + b_f - c_f

            da_b_d = '\\True $a + b - c = %s$' % (format_vn(tong))
            da_b_s = '$a + b - c = %s$' % (format_vn(tong + 100))
            list_da_b = [da_b_d, da_b_s]
            shuffled_b = random.choice(list_da_b)

            loigiai_b = ('''Lợi nhuận là $f(x) = R(x) - T(x) = %s x - (x^2 + %s x + %s) = -x^2 %s x - %s$. \\\\ Suy ra $a=-1, b=%s, c=-%s$. Vậy $a+b-c = -1 + (%s) - (-%s) = %s$.''' 
                        % (format_vn(doanh_thu_dung), m_goc, n_goc, format_vn(b_f), n_goc, format_vn(b_f), n_goc, format_vn(b_f), n_goc, format_vn(tong)))

            ########################################################################
            # c) Điều kiện lãi
            delta = b_f**2 - 4*a_f*c_f

            da_c_s = 'Để công ty có lãi thì số sản phẩm bán ra thỏa mãn $50 < x < 70$'
            da_c_d = '\\True Công ty không thể có lãi với mọi số lượng sản phẩm $x \\ge 0$'
            list_da_c = [da_c_d, da_c_s]
            shuffled_c = random.choice(list_da_c)

            loigiai_c = ('''Để công ty có lãi thì $f(x) > 0 \\Leftrightarrow -x^2 %s x - %s > 0$. Tam thức bậc hai này có $\\Delta = (%s)^2 - 4(-1)(-%s) = %s < 0$. Vì hệ số $a=-1 < 0$ nên $f(x) < 0$ với mọi $x$. Vậy công ty luôn lỗ.''' 
                        % (format_vn(b_f), n_goc, format_vn(b_f), n_goc, format_vn(delta)))

            ########################################################################
            # d) Cực trị
            x_max = -b_f / (2*a_f)
            y_max = a_f*(x_max**2) + b_f*x_max + c_f

            da_d_s = 'Lợi nhuận lớn nhất vượt quá $240$ triệu đồng'
            da_d_d = '\\True Lợi nhuận lớn nhất không vượt quá $0$ triệu đồng'
            list_da_d = [da_d_d, da_d_s]
            shuffled_d = random.choice(list_da_d)

            loigiai_d = ('''Vì $f(x)$ luôn âm nên lợi nhuận lớn nhất đạt tại đỉnh Parabol $x = \\frac{-b}{2a} = %s$. Giá trị lợi nhuận khi đó là $f(%s) \\approx %s < 0$.''' 
                        % (format_vn(round(x_max, 2)), format_vn(round(x_max, 2)), format_vn(round(y_max, 2))))

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_a)+'}\n'
                '{'+str(shuffled_b)+'}\n'
                '{'+str(shuffled_c)+'}\n'
                '{'+str(shuffled_d)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_a)+'\n'
                '\\item '+str(loigiai_b)+'\n'
                '\\item '+str(loigiai_c)+'\n'
                '\\item '+str(loigiai_d)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

