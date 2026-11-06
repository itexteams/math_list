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


def bt_dang5_p1_b5_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(5,19)

                du = ['$%s \\sqrt{7}$'%(latex(a)),
                    ]
                da= random.choice(du)
                s = ['$%s \\sqrt{7}$'%(latex(a+1)),
                    '$%s \\sqrt{5}$'%(latex(a+2)),
                    '$%s \\sqrt{5}$'%(latex(a+3)),
                    '$%s \\sqrt{5}$'%(latex(a-1)),
                    '$%s \\sqrt{7}$'%(latex(a-2)),
                    '$%s \\sqrt{7}$'%(latex(a-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AD = %s, CD = %s, AA' = %s \\sqrt{2}$. Đường chéo $AC'$ có độ dài bằng'''
                                %(latex(2*a),latex(a),latex(a)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                        \\clip(-1.0519842992053314,-0.6061792383769713) rectangle (7.238222702540806,3.9527561995718);
                        \\draw [line width=1.pt ,dashed] (0.,0.)-- (2.,1.);
                        \\draw [line width=1.pt ,dashed] (2.,1.)-- (6.,1.);
                        \\draw [line width=1.pt ] (6.,1.)-- (4.,0.);
                        \\draw [line width=1.pt ] (4.,0.)-- (0.,0.);
                        \\draw [line width=1.pt ,dashed] (2.,1.)-- (2.,3.);
                        \\draw [line width=1.pt ] (2.,3.)-- (0.,2.);
                        \\draw [line width=1.pt ] (0.,2.)-- (0.,0.);
                        \\draw [line width=1.pt ] (2.,3.)-- (6.,3.);
                        \\draw [line width=1.pt ] (6.,3.)-- (4.,2.);
                        \\draw [line width=1.pt ] (4.,2.)-- (4.,0.);
                        \\draw [line width=1.pt ] (0.,2.)-- (4.,2.);
                        \\draw [line width=1.pt ] (6.,3.)-- (6.,1.);
                        \\draw [line width=1.pt ,dashed] (2.,1.)-- (4.,2.);
                        \\draw [line width=1.pt ,dashed] (2.,1.)-- (4.,0.);
                        \\draw (1.5259851448728454,1.5783106589734817) node[anchor=north west] {$A$};
                        \\draw (-0.536390410389696,0.31646245739837525) node[anchor=north west] {$B$};
                        \\draw (4.049681548023061,0.1400750743825002) node[anchor=north west] {$C$};
                        \\draw (6.0713523225896315,1.415491536189597) node[anchor=north west] {$D$};
                        \\draw (1.6345312267287688,3.7356640358599535) node[anchor=north west] {$A'$};
                        \\draw (-0.5499586706216864,2.7180445184606743) node[anchor=north west] {$B'$};
                        \\draw (3.7104750422233006,2.772317559388636) node[anchor=north west] {$C'$};
                        \\draw (6.057784062357641,3.61354969377204) node[anchor=north west] {$D'$};
                \\end{tikzpicture}
            \\end{center}
                        $AC' = \\sqrt{AB^2 + AD^2 + AA'^2} = \\sqrt{%s^2 + %s^2 + (%s \\sqrt{2})^2} = %s \\sqrt{7}$.'''
                        %(latex(a),latex(2*a),latex(a),latex(a)
                        ))

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

