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


def bt_dang7_p3_b4_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a1=randint(20,70)
                b1=randint(20,60)
                a=2*a1
                b=2*b1
                while a-5<=b:
                    a1=randint(20,70)
                    b1=randint(20,60)
                    a=2*a1
                    b=2*b1
                smax=2*a1*b1
                # Câu hỏi
                noidungcauhoi = ('Một mảnh đất hình Elip có độ dài trục lớn bằng $%s$m, độ dài trục bé bằng $%s$m.'
                                ' Một tập đoàn dự định xây dựng một trung tâm thương mại trong một hình chữ nhật nội tiếp của hình elip như hình vẽ. Diện tích xây dựng trung tâm thương mại lớn nhất bằng bao nhiêu mét vuông?'
                                '\\begin{center}'
                                '''\\scalebox{0.7}{
                                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-4.697115516195303,-2.644661868960699) rectangle (4.886889848201415,2.891440608610075);
                \\fill[color=ffqqqq,fill=ffqqqq,pattern=north east lines,pattern color=ffqqqq] (-1.8672907596244301,1.50220258604178) -- (1.8498737199514825,1.5129387331007274) -- (1.8874672365796827,-1.4895414446799153) -- (-1.874222959092389,-1.4978798849725854) -- cycle;
                \\draw [rotate around={0.:(0.,0.)},line width=1.6pt] (0.,0.) ellipse (2.8284271247461907cm and 2.cm);
                \\draw [color=ffqqqq] (-1.8672907596244301,1.50220258604178)-- (1.8498737199514825,1.5129387331007274);
                \\draw [color=ffqqqq] (1.8498737199514825,1.5129387331007274)-- (1.8874672365796827,-1.4895414446799153);
                \\draw [color=ffqqqq] (1.8874672365796827,-1.4895414446799153)-- (-1.874222959092389,-1.4978798849725854);
                \\draw [color=ffqqqq] (-1.874222959092389,-1.4978798849725854)-- (-1.8672907596244301,1.50220258604178);
                \\draw [->] (-3.5,0.) -- (3.5,0.);
                \\draw [->] (0.,-2.5) -- (0.,2.7058765321278297);
                \\draw (1.8,2) node[anchor=north west] {$M$};
                \\draw (3.1010503393076165,-0.1) node[anchor=north west] {$x$};
                \\draw (-0.5152746662023251,2.921204600424972) node[anchor=north west] {$y$};
                \\draw (-0.5301566621097734,0.07874338210234304) node[anchor=north west] {$O$};
                \\draw (1.865844678989406,0.07874338210234304) node[anchor=north west] {$x_M$};
                \\draw (-0.7,1.998520854163176) node[anchor=north west] {$y_M$};
            \\end{tikzpicture}}'''
            '\\end{center}'
                                %(latex(a),latex(b)))

                # Nội dung lời giải
                loigiai=('Phương trình chính tắc của elip $(E): \\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1$.\\\\ '
                        'Ta có $2a=%s\\Rightarrow a=%s$, $2b=%s\\Rightarrow b=%s$.\\\\ \n'
                        'Suy ra $(E): \\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}=1$.\\\\ \n'
                        'Chọn $M(x_M;y_M)$ là đỉnh hình chữ nhật và $x_M>0,y_M>0)$.\\\\ \n'
                        'Ta có $M$ thuộc $(E)$ nên $\\dfrac{x_{M}^2}{%s}+\\dfrac{y_{M}^2}{%s}=1$.\\\\ \n'
                        'Diện tích hình chữ nhật là\\\\ \n'
                        '$S=4x_M\\cdot y_M=%s\\cdot 2 \\cdot \\dfrac{x^2}{%s}\\cdot\\dfrac{y^2}{%s}\\le %s \\left(\\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}\\right)=%s$ m$^2$.\\\\ \n'
                        'Vậy diện tích xây dựng trung tâm thương mại lớn nhất bằng $%s$ m$^2$.'
                        %(latex(a),latex(a1),latex(b),latex(b1),

                        latex(a1**2),latex(b1**2),
                        latex(a1**2),latex(b1**2),

                        latex(smax),latex(a1),latex(b1),latex(smax),latex(a1**2),latex(b1**2),latex(smax),
                        latex(smax)
                        ))


                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(smax))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

