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


def bt_dang5_p3_b1_c5_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                lis=[2,3,6,4,5,7,11]
                a=random.choice(lis)
                lis.remove(a)
                ma=randint(2,3)
                ma1=ma-2

                b=random.choice(lis)
                lis.remove(b)
                mb=randint(2,3)
                mb1=mb-5
                mb2=mb-6

                c=random.choice(lis)
                lis.remove(c)
                mc=randint(-3,-2)
                mc1=mc+5

                d=random.choice(lis)
                md=randint(2,3)
                md1=md+1

                kqz=Rational(a**(ma-ma1)+b**(mb*mb1-mb*mb2),c**(mc+2*mc1)+d**(-md+2*md1))
                while kqz>=99.9:
                    lis=[2,3,6,4,5,7,11]
                    a=random.choice(lis)
                    lis.remove(a)
                    ma=randint(2,3)
                    ma1=ma-2

                    b=random.choice(lis)
                    lis.remove(b)
                    mb=randint(2,3)
                    mb1=mb-5
                    mb2=mb-6

                    c=random.choice(lis)
                    lis.remove(c)
                    mc=randint(-3,-2)
                    mc1=mc+5

                    d=random.choice(lis)
                    md=randint(2,3)
                    md1=md+1

                    kqz=Rational(a**(ma-ma1)+b**(mb*mb1-mb*mb2),c**(mc+2*mc1)+d**(-md+2*md1))

                hz=kqz
                number = Decimal(float(hz))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Câu hỏi
                noidungcauhoi = ('Giá trị biểu thức $P=\\dfrac{%s^%s \\cdot \\left( \\dfrac{1}{%s} \\right)^%s+\\left(%s^%s\\right)^{%s} \\cdot \\left( \\dfrac{1}{%s}\\right)^{%s}}{%s^{%s} \\cdot %s^%s+\\left(\\dfrac{1}{%s}\\right)^%s \\cdot %s^%s}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)zz'
                                %(latex(a),latex(ma),latex(a),latex(ma1),latex(b),latex(mb),latex(mb1),latex(b**mb),latex(mb2),latex(c),latex(mc),latex(c**2),latex(mc1),latex(d),latex(md),latex(d**2),latex(md1)
                                ))
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $P=\\dfrac{%s^%s \\cdot \\left( \\dfrac{1}{%s} \\right)^%s+\\left(%s^%s\\right)^{%s} \\cdot \\left( \\dfrac{1}{%s}\\right)^{%s}}{%s^{%s} \\cdot %s^%s+\\left(\\dfrac{1}{%s}\\right)^%s \\cdot %s^%s}=\\dfrac{%s^{%s} \\cdot %s^{%s}+%s^{%s} \\cdot %s^{%s}}{%s^{%s} \\cdot %s^{%s}+%s^{%s} \\cdot %s^{%s}}=\\dfrac{%s^{%s}+%s^{%s}}{%s^{%s}+%s^{%s}}=%s$zz'
                        %(latex(a),latex(ma),latex(a),latex(ma1),latex(b),latex(mb),latex(mb1),latex(b**mb),latex(mb2),latex(c),latex(mc),latex(c**2),latex(mc1),latex(d),latex(md),latex(d**2),latex(md1),
                        latex(a),latex(ma),latex(a),latex(-ma1),
                        latex(b),latex(mb*mb1),latex(b),latex(-mb*mb2),
                        latex(c),latex(mc),latex(c),latex(2*mc1),
                        latex(d),latex(-md),latex(d),latex(2*md1),
                        latex(a),latex(ma-ma1),latex(b),latex(mb*mb1-mb*mb2),
                        latex(c),latex(mc+2*mc1),latex(d),latex(-md+2*md1),
                        latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content   

