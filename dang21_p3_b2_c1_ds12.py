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


def bt_dang21_p3_b2_c1_ds12(self):
            # Khai báo biến
            gia = random.choice([150,160,170,180,190,200,210,220,230,240,250])
            x1 = random.choice([4,5,6,7])
            x2 = x1+random.choice([2,4,6,8])
            d = random.choice([-560,-550,-540,-530,-520,-510,-500,-480,-460,-450,-440,-420,-400])
            loi_nhuan = integrate(3*(x + x1)*(x2 - x)) + d 
            kq = loi_nhuan.subs(x,x2)
            while kq < 2 * gia:
                x1 = random.choice([4,5,6,7])
                x2 = x1+random.choice([2,4,6,8])
                d = random.choice([-560,-550,-540,-530,-520,-510,-500,-480,-460,-450,-440,-420,-400])
                loi_nhuan = integrate(3*(x + x1)*(x2 - x)) + d 
                kq = loi_nhuan.subs(x,x2)
            doanh_thu = gia*x
            chi_phi = doanh_thu - loi_nhuan
            noidungcauhoi = f"""Một hộ làm nghề dệt vải lụa tơ tằm, sản xuất mỗi ngày được $x$ mét vải \\text{{($1\\le x\\le {latex(2*x2-4)} $)}}$zz$ 
            Tổng chi phí sản xuất $x$ mét vải lụa, tính bằng nghìn đồng, cho bởi hàm chi phí \\text{{$C(x) = {latex(chi_phi)}$}}$zz$ 
            Giả sử hộ này bán hết sản phẩm đã dệt ra  mỗi ngày với giá ${gia} $ nghìn đồng/mét$zz$ 
            Lợi nhuận tối đa của hộ này thu được trong một ngày là bao nhiêu nghìn đồng?
            """
            loigiai = f""" 
            Bán hết $x$ mét vải thì thu được số tiền là $R(x) = {latex(doanh_thu)}$$zz$\\\\
            Hàm lợi nhuận $L(x) = R(x) - C(x) = {latex(loi_nhuan)}$$zz$\\\\
            Ta có $L'(x) = {latex(diff(loi_nhuan))}$$zz$\\\\
            $L'(x) = 0 \\Leftrightarrow x = {x2}$ và $x = {x1} $$zz$\\\\
            Ta có $L(1) = {latex(loi_nhuan.subs(x, 1))}$, $L({2*x2 - 4}) = {latex(loi_nhuan.subs(x, 2*x2 - 4))}$, $L({x1}) = {latex(loi_nhuan.subs(x, x1))}$ và $L({x2}) = {latex(loi_nhuan.subs(x, x2))}$$zz$\\\\
            Lợi nhuận tối đa của hộ này thu được trong một ngày là ${kq}$ nghìn đồng khi sản xuất và bán hết ${x2}$ mét vải$zz$
            """
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq))              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zz$','.').replace('\\frac','\\dfrac').replace('pht','\\%')
            return content

