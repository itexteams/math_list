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


def bt_dang5_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                n=symbols('n')
                a=randint(1,50)
                m=randint(-9,9)
                p=randint(-9,9)
                d=randint(-9,9)
                while m==0 or p==0:
                    n=symbols('n')
                    a=randint(1,50)
                    m=randint(-9,9)
                    p=randint(-9,9)
                    d=randint(-9,9)


                un1=(a*n-(a-1))
                un2=(a*n+1)

                u11=(a*1-(a-1))
                u12=(a*1+1)

                u21=(a*2-(a-1))
                u22=(a*2+1)

                u31=(a*3-(a-1))
                u32=(a*3+1)

                # Nội dung câu hỏi
                noidungcauhoi = ('Tính giới hạn $\\underset{n\\to +\\infty }{\\mathop{\\lim }}\\left[\\dfrac{1}{%s\\cdot %s}+\\dfrac{1}{%s\\cdot %s}+\\dfrac{1}{%s\\cdot %s}+\\cdots+\\dfrac{1}{(%s)(%s)}\\right]=\\dfrac{a}{b}$.\\\\ \n'
                                'Với $a\\in \\mathbb{Z}$; $b\\in \\mathbb{N}$ và $\\dfrac{a}{b}$ là là phân số tối giản. Giá trị biểu thức $%sa+%sb$ bằng bao nhiêu?'
                                %(latex(u11),latex(u12),latex(u21),latex(u22),latex(u31),latex(u32),latex(un1),latex(un2),latex(m),latex(p),))

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '$\\dfrac{1}{%s\\cdot %s}=\\dfrac{1}{%s}\\left(\\dfrac{1}{%s}-\\dfrac{1}{%s}\\right)$;\\hspace*{0.2cm}$\\dfrac{1}{%s\\cdot %s}=\\dfrac{1}{%s}\\left(\\dfrac{1}{%s}-\\dfrac{1}{%s}\\right)$;\\hspace*{0.2cm}$\\dfrac{1}{%s\\cdot %s}=\\dfrac{1}{%s}\\left(\\dfrac{1}{%s}-\\dfrac{1}{%s}\\right)$;\\\\ \n'
                        '$\\cdots$\\\\ \n'
                        '$\\cdots$\\\\ \n'
                        '$\\cdots$\\\\ \n'
                        '$\\dfrac{1}{(%s)\\cdot (%s)}=\\dfrac{1}{%s}\\left(\\dfrac{1}{%s}-\\dfrac{1}{%s}\\right)$. \\\\ \n'
                        'Khi đó $\\underset{n\\to +\\infty }{\\mathop{\\lim }}\\left[\\dfrac{1}{%s\\cdot %s}+\\dfrac{1}{%s\\cdot %s}+\\dfrac{1}{%s\\cdot %s}+\\cdots+\\dfrac{1}{(%s)(%s)}\\right]$\\\\ \n'
                        '\\hspace*{1cm}$=\\underset{n\\to +\\infty }{\\mathop{\\lim }}\\left[\\dfrac{1}{%s}\\left(\\dfrac{1}{%s}-\\dfrac{1}{%s}+\\dfrac{1}{%s}-\\dfrac{1}{%s}+\\cdots+\\dfrac{1}{%s}-\\dfrac{1}{%s}\\right)\\right]$\\\\ \n'
                        '\\hspace*{1cm}$=\\underset{n\\to +\\infty }{\\mathop{\\lim }}\\left[\\dfrac{1}{%s}\\left(1-\\dfrac{1}{%s}\\right)\\right]=\\dfrac{1}{%s}$. Suy ra $a=1$ và $b=%s$.\\\\ \n'
                        'Vậy $%s a +%s b=%s \\cdot 1 +%s \\cdot %s = %s$.'

                        %(latex(u11),latex(u12),latex(a),latex(u11),latex(u12),    latex(u21),latex(u22),latex(a),latex(u21),latex(u22),  latex(u31),latex(u32),latex(a),latex(u31),latex(u32),
                        latex(un1),latex(un2),latex(a),latex(un1),latex(un2),
                        latex(u11),latex(u12),latex(u21),latex(u22),latex(u31),latex(u32),latex(un1),latex(un2),
                        latex(a),latex(u11),latex(u12),latex(u21),latex(u22), latex(un1),latex(un2),
                        latex(a),latex(un2),latex(a),
                        latex(a),
                        latex(m),latex(p),latex(m),latex(p),latex(a),latex(m+p*a),
                        )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1a', 'a').replace('1b', 'b')
            return content    

