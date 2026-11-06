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


def bt_dang7_p4_b2_c4_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                lis=[0.3,0.5,0.6,0.7,0.8,0.9]
                a=random.choice(lis)
                pa=a/100
                p_a=1-pa

                b=randint(80,95)
                pb=b/100
                p_b=round(1-pb,2)


                c=randint(96,98)
                pc=c/100
                p_c=1-pc



                kq=(p_a*pc)/(p_a*pc+pa*p_b)

                kq1=round(kq*100,2)

                # Câu hỏi
                noidungcauhoi = ('Một thống kê cho thấy tỉ lệ dân số mắc bệnh hiểm nghèo Y là $%s$phtrzz Bà N đi xét nghiệm bệnh hiểm nghèo Y và nhận được kết quả là âm tínhzz Biết rằng, nếu mắc bệnh hiểm nghèo Y thì với xác suất $%s$ xét nghiệm là dương tính; nếu không bị bệnh hiểm nghèo Y thì với xác suất $%s$ xét nghiệm là âm tínhzz Sau khi xét nghiệm cho kết quả âm tính, tính xác suất không mắc bệnh hiểm nghèo Y của bà Nzz'
                                %(latex(a),latex(pb),latex(pb)
                                ))

                # Nội dung lời giải
                loigiai=('Gọi các biến cố: \\\\ \n'
                        '\\hspace*{1cm} $A$:"Bà N bị bệnh hiểm ngèo Y"zz \\\\ \n'
                        '\\hspace*{1cm} $B$:"Xét nghiệm cho kết quả dương tính"zz \\\\ \n'
                        'Trước khi tiến hành xét nghiệm, xác suất không mắc bệnh hiểm nghèo Y của bà N là \n'
                        '$$P(\\overline{A})=1-P(A)=1-%s=%szz$$'            

                        'Ta cần tính $P(\\overline{A}| \\overline{B})$zz Theo công thức Bayes \n'           
                        '$$P(\\overline{A}| \\overline{B})=\\dfrac{P(\\overline{A}) \\cdot P(\\overline{B}| \\overline{A})}{P(\\overline{A}) \\cdot P(\\overline{B}| \\overline{A})+P(A) \\cdot P(\\overline{B}| A)}zz$$ \n'
                        '$P(\\overline{B}| \\overline{A})$ là xác suất để bà N có xét nghiệm âm tính nếu bà N không mắc bệnh Yzz \\\\ \n'                          
                        'Ta có $P(\\overline{B}| \\overline{A})=%s$zz \\\\ \n'

                        '$P(\\overline{B}| A)$ là xác suất để bà N có xét nghiệm âm tính nếu bà N bị bệnh Yzz \\\\ \n'                          
                        'Ta có $P(\\overline{B}| A)=1-%s=%s$zz \\\\ \n'

                        'Thay vào công thức Bayes ta có  \n'
                        '$$P(\\overline{A}| \\overline{B})=\\dfrac{%s \\cdot %s}{%s \\cdot %s+%s \\cdot %s}=%szz$$ \n'
                        'Vậy xác suất không mắc bệnh hiểm nghèo Y của bà N là $%s$phtr zz'
                        %(latex(pa),latex(p_a),
                        latex(pc),
                        latex(pb),latex(p_b),
                        latex(p_a),latex(pc),latex(p_a),latex(pc),latex(pa),latex(p_b),
                        latex(kq),
                        latex(kq1)


                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.').replace('phtr', '\\%')
            return content 

