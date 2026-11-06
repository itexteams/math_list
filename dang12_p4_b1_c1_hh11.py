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


def bt_dang12_p4_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':

                # Các đối tượng hình học (chỉ dùng để điền vào câu hỏi)
                diem_I = r'I \in SA, SA=3IA'
                diem_J = r'J \in SC'
                diem_M = r'M \text{ là trung điểm của } SB'
                mp_IJM = r'(IJM)'
                dt_AB = r'AB'

                # Kết quả cần tìm
                kq_diem = r'E'

                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$. 
                                 Lấy $I$ thuộc $SA$ sao cho $SA=3IA$, $J$ thuộc $SC$ sao cho $SC=3JC$ và $M$ là trung điểm của $SB$.\\\\ 
                                 a) Tìm giao điểm của $AB$ và $(IJM)$.\\\\
                                 b) Tìm giao điểm của $BC$ và $(IJM)$.''')

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                           \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,scale=0.7]
            					\\clip(-6.949,-2.8558) rectangle (7.9824,4.985);
            					\\draw [dash pattern=on 1pt off 1pt] (0.,0.)-- (6.02,0.);
            					\\draw (0.,0.)-- (2.,-2.);
            					\\draw (2.,-2.)-- (5.,-2.);
            					\\draw (5.,-2.)-- (6.02,0.);
            					\\draw (2.,4.)-- (0.,0.);
            					\\draw (2.,4.)-- (2.,-2.);
            					\\draw (2.,4.)-- (5.,-2.);
            					\\draw (2.,4.)-- (6.02,0.);
            					\\draw (-5.905876777251182,0.)-- (1.,2.);
            					\\draw [dash pattern=on 1pt off 1pt] (1.,2.)-- (3.3314239999999997,2.6752);
            					\\draw (2.,2.018378378378378)-- (-1.9458598726114655,1.9458598726114655);
            					\\draw (-1.95,1.95)-- (-1.33,1.33);
            					\\draw (-5.905876777251182,0.)-- (0.,0.);
            					\\draw [dash pattern=on 1pt off 1pt] (2.,2.018378378378378)-- (3.3314239999999997,2.6752);
            					\\draw [dash pattern=on 1pt off 1pt] (0.,0.)-- (-1.9458598726114655,1.9458598726114655);
            					\\draw (1.6904,4.864) node[anchor=north west] {$S$};
            					\\draw (-0.6,0) node[anchor=north west] {$B$};
            					\\draw (6,0.5806) node[anchor=north west] {$A$};
            					\\draw (4.8364,-1.9) node[anchor=north west] {$D$};
            					\\draw (1.42,-1.9) node[anchor=north west] {$C$};
            					\\draw (3.3,3.5814) node[anchor=north west] {$I$};
            					\\draw (1.4,1.9) node[anchor=north west] {$J$};
            					\\draw (0.3,2.928) node[anchor=north west] {$M$};
            					\\draw (-2.4236,2.7) node[anchor=north west] {$F$};
            					\\draw (-6.6828,0.508) node[anchor=north west] {$E$};
            				\\end{tikzpicture}
                           \\end{center}'''
                    '''a) Trong mặt phẳng $(SAB)$ kẻ $IM$ cắt $AB$ tại $E$.\\\\
                              Khi đó $E\\in AB$, $E\\in MI\\subset (IJM)\\Rightarrow E\\in (IJM)$.\\\\
                                  Vậy $E$ là giao điểm của $AB$ và $\\left( IJM \\right)$.\\\\
                            b) Trong mặt phẳng $(SBC)$ kẻ $JM$ cắt $BC$ tại $F$.\\\\
                            Khi đó $F\\in BC$, $F\\in MJ\\subset (IJM)\\Rightarrow F\\in (IJM)$.\\\\
                            Vậy $F$ là giao điểm của $AB$ và $\\left( IJM \\right)$.''')

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

