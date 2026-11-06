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


def bt_dang9_p4_b1_c1_hh10(self):
            # Khai báo biến
            lis0=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
            goc=random.choice(lis0)

            lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
            a=random.choice(lis)
            b=random.choice(lis)
            c=random.choice(lis)
            while a-b==0 or a-c==0 or b-c==0:
                a=random.choice(lis)
                b=random.choice(lis)
                c=random.choice(lis)

            kq=Rational((a+c)*goc**2+b*goc+c,1+goc**2)       
            lis=['1','2']
            dang=random.choice(lis)
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\cot a = %s$. Tính giá trị biểu thức $P=%s \\cos^{2}a +%s \\sin a \\cos a +%s$.'''
                            %(latex(goc),latex(a),latex(b),latex(c)
                                ))

                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=%s \\cos^{2}a +%s \\sin a \\cos a +%s = \\sin^{2}a \\left( %s \\cot^{2}a +%s \\cot a +\\dfrac{%s}{\\sin^{2}a} \\right)$ \\\\ \n'
                        '$P = \\dfrac{1}{1+\\cot^{2}a} \\left( %s \\cot^{2}a +%s \\cot a +%s \\right)= \\dfrac{1}{1+(%s)^2} \\left( %s \\cdot (%s)^2 +%s \\cdot (%s) +%s \\right) =%s$.'
                        %(latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),
                        latex(a+c),latex(b),latex(c),latex(goc),latex(a+c),latex(goc),latex(b),latex(goc),latex(c),latex(kq)
                            ))
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\tan a = %s$. Tính giá trị biểu thức $P=%s \\sin^{2}a +%s \\sin a \\cos a +%s$.'''
                            %(latex(goc),latex(a),latex(b),latex(c)
                                ))

                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$P=%s \\sin^{2}a +%s \\sin a \\cos a +%s = \\cos^{2}a \\left( %s \\tan^{2}a +%s \\tan a +\\dfrac{%s}{\\cos^{2}a} \\right)$ \\\\ \n'
                        '$P = \\dfrac{1}{1+\\tan^{2}a} \\left( %s \\tan^{2}a +%s \\tan a +%s \\right)= \\dfrac{1}{1+(%s)^2} \\left( %s \\cdot (%s)^2 +%s \\cdot (%s) +%s \\right) =%s$.'
                        %(latex(a),latex(b),latex(c),latex(a),latex(b),latex(c),
                        latex(a+c),latex(b),latex(c),latex(goc),latex(a+c),latex(goc),latex(b),latex(goc),latex(c),latex(kq)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content

