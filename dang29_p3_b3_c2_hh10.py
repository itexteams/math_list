
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


def bt_dang29_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        F0=random.choice([10,12,15,16,18,20,24,25,30,35,40,45,50])
        k=random.choice([2,3,4,5])
        alpha=random.choice([30,45])
        ten_k={2:'gấp đôi',3:'gấp ba',4:'gấp bốn',5:'gấp năm'}[k]
        oe_val=2*F0*cos(alpha*pi/180)
        f1_val=oe_val/Rational(k-1,1)
        f2_val=k*f1_val
        number=Decimal(float(f2_val))
        kq=number.quantize(Decimal('0.1'),rounding=ROUND_HALF_UP)
        kq_vn=str(kq).replace('.','{,}')
        hs_k1='' if k-1==1 else str(k-1)
        hinh_de=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\draw (0,0) circle (1.2);\n'
        '\\draw[->] (0,0)--(2.4,0);\n'
        '\\draw[->] (0,0)--(-4.2,0);\n'
        '\\draw[dashed,->] (0,0)--(%s:2.1);\n'
        '\\draw[dashed,->] (0,0)--(-%s:2.1);\n'
        '\\node[above left] at (0,0) {$O$};\n'
        '\\node[above] at (1.8,0) {$\\overrightarrow{F_1}$};\n'
        '\\node[above] at (-3.5,0) {$\\overrightarrow{F_2}$};\n'
        '\\node[above] at (%s:2.1) {$\\overrightarrow{F_3}$};\n'
        '\\node[below right] at (-%s:2.1) {$\\overrightarrow{F_4}$};\n'
        '\\node at (%s:0.8) {\\scriptsize $%s^\\circ$};\n'
        '\\node at (-%s:0.8) {\\scriptsize $%s^\\circ$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(alpha,alpha,alpha,alpha,alpha/2,alpha,alpha/2,alpha)
        hinh_lg=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\draw (0,0) circle (1.2);\n'
        '\\draw[->] (0,0)--(2.4,0) node[right] {$A$};\n'
        '\\draw[->] (0,0)--(-4.2,0) node[left] {$B$};\n'
        '\\draw[dashed,->] (0,0)--(%s:2.1) node[above right] {$C$};\n'
        '\\draw[dashed,->] (0,0)--(-%s:2.1) node[below right] {$D$};\n'
        '\\node[above left] at (0,0) {$O$};\n'
        '\\node[above] at (1.8,0) {$\\overrightarrow{F_1}$};\n'
        '\\node[above] at (-3.5,0) {$\\overrightarrow{F_2}$};\n'
        '\\node[right] at (%s:1.65) {$\\overrightarrow{F_3}$};\n'
        '\\node[right] at (-%s:1.65) {$\\overrightarrow{F_4}$};\n'
        '\\node at (%s:0.8) {\\scriptsize $%s^\\circ$};\n'
        '\\node at (-%s:0.8) {\\scriptsize $%s^\\circ$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(alpha,alpha,alpha,alpha,alpha/2,alpha,alpha/2,alpha)
        noidungcauhoi=('Một vật đang ở vị trí $O$ chịu hai lực tác dụng ngược chiều nhau là $\\overrightarrow{F_1}$ và $\\overrightarrow{F_2}$, trong đó độ lớn lực $\\overrightarrow{F_2}$ lớn %s độ lớn lực $\\overrightarrow{F_1}$. Người ta muốn vật dừng lại nên cần tác dụng vào vật hai lực $\\overrightarrow{F_3},\\overrightarrow{F_4}$ có phương hợp với lực $\\overrightarrow{F_1}$ các góc $%s^\\circ$ như hình vẽ, chúng có độ lớn bằng nhau và bằng $%s\\text{ N}$. Tìm độ lớn của lực $\\overrightarrow{F_2}$ (kết quả làm tròn đến một chữ số sau dấu phẩy).\n'%(ten_k,alpha,F0)+hinh_de).replace('- -','+').replace('+ -','-')
        if alpha==45:
            loai_hinh='hình vuông'
            tinh_oe='OE=%s\\sqrt{2}'%(F0)
        else:
            loai_hinh='hình thoi'
            tinh_oe='OE=2\\cdot OC\\cdot\\cos 30^\\circ=%s\\sqrt{3}'%(F0)
        loigiai=(hinh_lg+'Ta có: $\\overrightarrow{F_2}=-%s\\overrightarrow{F_1}$. Để vật trở về trạng thái cân bằng thì hợp lực bằng $\\overrightarrow{0}$.\\\\\n$\\Leftrightarrow \\overrightarrow{F_1}+\\overrightarrow{F_2}+\\overrightarrow{F_3}+\\overrightarrow{F_4}=\\overrightarrow{0}\\Leftrightarrow \\overrightarrow{F_1}-%s\\overrightarrow{F_1}+\\overrightarrow{F_3}+\\overrightarrow{F_4}=\\overrightarrow{0}\\Leftrightarrow \\overrightarrow{F_3}+\\overrightarrow{F_4}=%s\\overrightarrow{F_1}$.\\\\\nĐặt $\\overrightarrow{F_1}=\\overrightarrow{OA},\\overrightarrow{F_2}=\\overrightarrow{OB},\\overrightarrow{F_3}=\\overrightarrow{OC},\\overrightarrow{F_4}=\\overrightarrow{OD}$ và dựng hình bình hành $OCED$ suy ra $\\overrightarrow{OC}+\\overrightarrow{OD}=\\overrightarrow{OE}$.\\\\\nMặt khác: $OC=OD=%s$ và $\\widehat{COD}=%s^\\circ+%s^\\circ=%s^\\circ$ nên $OCED$ là %s, suy ra $%s$.\\\\\nVì $\\overrightarrow{OE}=%s\\overrightarrow{F_1}$ nên $|\\overrightarrow{F_1}|=%s\\text{ N}$, do đó $|\\overrightarrow{F_2}|=%s|\\overrightarrow{F_1}|=%s\\text{ N}\\approx %s\\text{ N}$.'%(k,k,hs_k1,F0,alpha,alpha,2*alpha,loai_hinh,tinh_oe,hs_k1,latex(f1_val),k,latex(f2_val),kq_vn)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
