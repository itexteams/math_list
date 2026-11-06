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


def bt_dang1_p3_b1_c5_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                ad=randint(5,30)
                ab=randint(5,30)
                bd=randint(5,30)
                ac=randint(5,30)
                bc=randint(5,30)
                cd=randint(5,30)
                tong=ad+ab+bd+ac+bc+cd
                t1=ab+bd+ac+cd
                t2=ad+bd+ac+bc
                t3=ad+ab+bc+cd
                h1=max(t1,t2,t3)
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                '''Một trò chơi điện tử quy định như sau: Có $4$ trụ $A, B,C, D$ với số
                                lượng các thử thách trên đường đi giữa các cặp trụ được mô tả trong
                                hình bên. Người chơi xuất phát từ một trụ nào đó, đi qua tất cả các
                                trụ còn lại, mỗi khi đi qua một trụ thì trụ đó sẽ bị phá hủy và không
                                thể quay trở lại trụ đó được nữa, nhưng người chơi vẫn phải trở về
                                trụ ban đầu. Tổng số thử thách của đường đi thoả mãn điều kiện
                                trên nhận giá trị lớn nhất là bao nhiêu?'''
                                '}{'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                    '\\clip(-0.9398354377154291,-0.7320627682347045) rectangle (5.845120619471604,3.799107885608467); \n'
                                    '\\draw [line width=1.pt] (0.,0.)-- (1.,3.); \n'
                                    '\\draw [line width=1.pt] (1.,3.)-- (5.,0.); \n'
                                    '\\draw [line width=1.pt] (5.,0.)-- (0.,0.); \n'
                                    '\\draw [line width=1.pt] (1.,3.)-- (2.,1.); \n'
                                    '\\draw [line width=1.pt] (2.,1.)-- (0.,0.); \n'
                                    '\\draw [line width=1.pt] (2.,1.)-- (5.,0.); \n'
                                    '\\draw (0.771153481053475,3.5985091847872845) node[anchor=north west] {$A$}; \n'
                                    '\\draw (-0.6,0.1647314236717565) node[anchor=north west] {$B$}; \n'
                                    '\\draw (4.948326427565144,0.09393188220545694) node[anchor=north west] {$C$}; \n'
                                    '\\draw (1.7977468323148174,1) node[anchor=north west] {$D$}; \n'
                                    '\\draw (1.6089480550713522,2.1) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (-0.007641475075819259,2.2) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (0.8419530225197744,1.2) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.78894041284301,2.1825183554612937) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.198944233957181,0.03493226431687398) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.9659392665087587,1.1559250041999503) node[anchor=north west] {$%s$}; \n'
                                '\\end{tikzpicture} \n'
                                '}'
                                %(latex(ad),latex(ab),latex(bd),latex(ac),latex(bc),latex(cd),
                                ))

                # Nội dung lời giải
                loigiai = ('Mỗi cách đi thỏa mãn yêu cầu bài toán là một hình gồm $4$ cạnh khép kín trong $6$ cạnh được tạo ra bỏ đi hai cạnh không chung đỉnh. \\\\ \n'
                        'Tổng số thử thách trên $6$ đường đi là \\\\ \n'
                        '\\hspace*{1cm} $%s+%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $AD$ và $BC$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $AB$ và $CD$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $AC$ và $BD$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s=%s$. \\\\ \n'
                        'Vậy tổng số thử thách lớn nhất là $%s$.'


                        %(latex(ad),latex(ab),latex(bd),latex(ac),latex(bc),latex(cd),latex(tong),
                            latex(tong),latex(ad),latex(bc),latex(t1),
                            latex(tong),latex(ab),latex(cd),latex(t2),
                            latex(tong),latex(ac),latex(bd),latex(t3),
                            latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='1':
                ad=randint(5,30)
                ab=randint(5,30)
                bd=randint(5,30)
                ac=randint(5,30)
                bc=randint(5,30)
                cd=randint(5,30)
                tong=ad+ab+bd+ac+bc+cd
                t1=ab+bd+ac+cd
                t2=ad+bd+ac+bc
                t3=ad+ab+bc+cd
                h1=min(t1,t2,t3)
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                '''Một trò chơi điện tử quy định như sau: Có $4$ trụ $A, B,C, D$ với số
                                lượng các thử thách trên đường đi giữa các cặp trụ được mô tả trong
                                hình bên. Người chơi xuất phát từ một trụ nào đó, đi qua tất cả các
                                trụ còn lại, mỗi khi đi qua một trụ thì trụ đó sẽ bị phá hủy và không
                                thể quay trở lại trụ đó được nữa, nhưng người chơi vẫn phải trở về
                                trụ ban đầu. Tổng số thử thách của đường đi thoả mãn điều kiện
                                trên nhận giá trị nhỏ nhất là bao nhiêu?'''
                                '}{'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                    '\\clip(-0.9398354377154291,-0.7320627682347045) rectangle (5.845120619471604,3.799107885608467); \n'
                                    '\\draw [line width=1.pt] (0.,0.)-- (1.,3.); \n'
                                    '\\draw [line width=1.pt] (1.,3.)-- (5.,0.); \n'
                                    '\\draw [line width=1.pt] (5.,0.)-- (0.,0.); \n'
                                    '\\draw [line width=1.pt] (1.,3.)-- (2.,1.); \n'
                                    '\\draw [line width=1.pt] (2.,1.)-- (0.,0.); \n'
                                    '\\draw [line width=1.pt] (2.,1.)-- (5.,0.); \n'
                                    '\\draw (0.771153481053475,3.5985091847872845) node[anchor=north west] {$A$}; \n'
                                    '\\draw (-0.6,0.1647314236717565) node[anchor=north west] {$B$}; \n'
                                    '\\draw (4.948326427565144,0.09393188220545694) node[anchor=north west] {$C$}; \n'
                                    '\\draw (1.7977468323148174,1) node[anchor=north west] {$D$}; \n'
                                    '\\draw (1.6089480550713522,2.1) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (-0.007641475075819259,2.2) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (0.8419530225197744,1.2) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.78894041284301,2.1825183554612937) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.198944233957181,0.03493226431687398) node[anchor=north west] {$%s$}; \n'
                                    '\\draw (2.9659392665087587,1.1559250041999503) node[anchor=north west] {$%s$}; \n'
                                '\\end{tikzpicture} \n'
                                '}'
                                %(latex(ad),latex(ab),latex(bd),latex(ac),latex(bc),latex(cd),
                                ))

                # Nội dung lời giải
                loigiai = ('Mỗi cách đi thỏa mãn yêu cầu bài toán là một hình gồm $4$ cạnh khép kín trong $6$ cạnh được tạo ra bỏ đi hai cạnh không chung đỉnh. \\\\ \n'
                        'Tổng số thử thách trên $6$ đường đi là \\\\ \n'
                        '\\hspace*{1cm} $%s+%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $AD$ và $BC$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $AB$ và $CD$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s=%s$. \\\\ \n'
                        'Bỏ đi hai cạnh $AC$ và $BD$ thì tổng số thử thách là \\\\ \n'
                        '\\hspace*{1cm} $%s-%s-%s=%s$. \\\\ \n'
                        'Vậy tổng số thử thách nhỏ nhất là $%s$.'


                        %(latex(ad),latex(ab),latex(bd),latex(ac),latex(bc),latex(cd),latex(tong),
                            latex(tong),latex(ad),latex(bc),latex(t1),
                            latex(tong),latex(ab),latex(cd),latex(t2),
                            latex(tong),latex(ac),latex(bd),latex(t3),
                            latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

