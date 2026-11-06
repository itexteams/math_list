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


def bt_dang12_p1_b1_c2_hh10(self):
            # Khai báo biến
            d = ['$\\overrightarrow{BQ}=\\overrightarrow{CP}$',
                '$\\overrightarrow{QB}=\\overrightarrow{PC}$',
                '$\\overrightarrow{BC}=\\overrightarrow{QP}$',
                '$\\overrightarrow{CB}=\\overrightarrow{PQ}$',
                '$\\overrightarrow{QN}=\\overrightarrow{AC}$',
                '$\\overrightarrow{NQ}=\\overrightarrow{CA}$',
                '$\\overrightarrow{QA}=\\overrightarrow{NC}$',
                '$\\overrightarrow{AQ}=\\overrightarrow{CM}$',
                '$\\overrightarrow{AB}=\\overrightarrow{PN}$',
                '$\\overrightarrow{BA}=\\overrightarrow{NP}$',
                '$\\overrightarrow{AP}=\\overrightarrow{BN}$',
                '$\\overrightarrow{PA}=\\overrightarrow{NB}$',
                '$\\overrightarrow{AQ}=\\overrightarrow{MB}$',
                '$\\overrightarrow{QA}=\\overrightarrow{BM}$',
                '$\\overrightarrow{BQ}=\\overrightarrow{MA}$',
                '$\\overrightarrow{QB}=\\overrightarrow{AM}$',
                '$\\overrightarrow{PC}=\\overrightarrow{AM}$',
                '$\\overrightarrow{CP}=\\overrightarrow{MA}$',
                '$\\overrightarrow{MC}=\\overrightarrow{AP}$',
                '$\\overrightarrow{PA}=\\overrightarrow{CM}$',
                '$\\overrightarrow{MC}=\\overrightarrow{BN}$',
                '$\\overrightarrow{NB}=\\overrightarrow{CM}$',
                '$\\overrightarrow{BM}=\\overrightarrow{NC}$',
                '$\\overrightarrow{CN}=\\overrightarrow{MB}$',
                ]
            da= random.choice(d)
            s = ['$\\overrightarrow{BQ}=\\overrightarrow{CN}$',
                '$\\overrightarrow{QB}=\\overrightarrow{CP}$',
                '$\\overrightarrow{BC}=\\overrightarrow{QA}$',
                '$\\overrightarrow{CB}=\\overrightarrow{PN}$',
                '$\\overrightarrow{QN}=\\overrightarrow{CA}$',
                '$\\overrightarrow{NQ}=\\overrightarrow{CP}$',
                '$\\overrightarrow{QA}=\\overrightarrow{NB}$',
                '$\\overrightarrow{AQ}=\\overrightarrow{CM}$',
                '$\\overrightarrow{AB}=\\overrightarrow{PC}$',
                '$\\overrightarrow{BA}=\\overrightarrow{PN}$',
                '$\\overrightarrow{AP}=\\overrightarrow{BC}$',
                '$\\overrightarrow{PA}=\\overrightarrow{NC}$',
                '$\\overrightarrow{AQ}=\\overrightarrow{MC}$',
                '$\\overrightarrow{QA}=\\overrightarrow{BN}$',
                '$\\overrightarrow{BQ}=\\overrightarrow{MC}$',
                '$\\overrightarrow{QB}=\\overrightarrow{MA}$',
                '$\\overrightarrow{PC}=\\overrightarrow{AB}$',
                '$\\overrightarrow{CP}=\\overrightarrow{MN}$',
                '$\\overrightarrow{MC}=\\overrightarrow{PA}$',
                '$\\overrightarrow{PA}=\\overrightarrow{CN}$',
                '$\\overrightarrow{MC}=\\overrightarrow{BC}$',
                '$\\overrightarrow{NB}=\\overrightarrow{CQ}$',
                '$\\overrightarrow{BM}=\\overrightarrow{NP}$',
                '$\\overrightarrow{CN}=\\overrightarrow{MA}$',
                ]
            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Câu hỏi
                noidungcauhoi='''Cho tam giác $ABC$ với điểm $M$ nằm trong tam giác. Gọi $A\', B\', C\'$ lần lượt là trung điểm của $BC, CA, AB$ và $N, P, Q$ là các điểm đối xứng với $M$ qua $A\', B\', C\'$. Khẳng định nào sau đây đúng? \n'''
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]   \n'
                                '\\clip(-1.2609269910286274,-1.9736011123551316) rectangle (6.963956361221837,4.691917738167552); \n'
                                '\\draw (2.,4.)-- (0.,0.); \n'
                                '\\draw (2.,4.)-- (6.,0.); \n'
                                '\\draw (0.,0.)-- (6.,0.); \n'
                                '\\draw (2.33172651785401,1.2980067638188464)-- (5.66827348214599,2.7019932361811536);  \n'
                                '\\draw (2.33172651785401,1.2980067638188464)-- (-0.3317265178540101,2.7019932361811536);  \n'
                                '\\draw (-0.3317265178540101,2.7019932361811536)-- (5.66827348214599,2.7019932361811536); \n'
                                '\\draw (2.33172651785401,1.2980067638188464)-- (3.66827348214599,-1.2980067638188464); \n'
                                '\\draw (5.66827348214599,2.7019932361811536)-- (3.66827348214599,-1.2980067638188464); \n'
                                '\\draw (3.66827348214599,-1.2980067638188464)-- (-0.3317265178540101,2.7019932361811536); \n'
                                '\\draw (-0.3317265178540101,2.7019932361811536)-- (0.,0.); \n'
                                '\\draw (5.66827348214599,2.7019932361811536)-- (6.,0.); \n'
                                '\\draw (-0.3317265178540101,2.7019932361811536)-- (2.,4.); \n'
                                '\\draw (3.66827348214599,-1.2980067638188464)-- (6.,0.); \n'
                                '\\draw (2.,4.)-- (2.33172651785401,1.2980067638188464); \n'
                                '\\draw (2.33172651785401,1.2980067638188464)-- (0.,0.); \n'
                                '\\draw (2.33172651785401,1.2980067638188464)-- (6.,0.); \n'
                                '\\draw (2.,4.)-- (5.66827348214599,2.7019932361811536); \n'
                                '\\draw (3.66827348214599,-1.2980067638188464)-- (0.,0.); \n'
                                '\\draw (-0.49653262743657683,0.10555155661524694) node[anchor=north west] {$A$}; \n'
                                '\\draw (1.7507868015240518,4.676629850895711) node[anchor=north west] {$B$}; \n'
                                '\\draw (6.199561997629786,0.12083944388708796) node[anchor=north west] {$C$}; \n'
                                '\\draw (3.8910910195817934,2.689204505556379) node[anchor=north west] {$A\'$}; \n'
                                '\\draw (3.004393557815015,0.6100518365860006) node[anchor=north west] {$B\'$}; \n'
                                '\\draw (0.604195256135976,2.7044923928282203) node[anchor=north west] {$C\'$}; \n'
                                '\\draw (5.633910168571669,3.3312957709737017) node[anchor=north west] {$N$}; \n'
                                '\\draw (3.524181725057609,-1.2856461851222858) node[anchor=north west] {$P$}; \n'
                                '\\draw (-0.8175782601452382,3.224280560070815) node[anchor=north west] {$Q$}; \n'
                                '\\draw (2.3164386305821694,1.9859616910516922) node[anchor=north west] {$M$}; \n'
                            '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                        'Từ hình vẽ ta có các tứ giác sau là hình bình hành. \\\\ \n'
                        '$BCPQ, ACNQ, ABNP, AMBQ, AMCP, BNCM$.'

                        )

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

