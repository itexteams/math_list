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


def bt_dang5_p4_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':

                # --- Khai báo biến (Dành cho mô phỏng bài tự luận) ---

                # Giả định các điểm I, J, M, N, E, F
                I_point = 'I'
                J_point = 'J'
                M_point = 'M'
                N_point = 'N'
                E_point = 'E'
                F_point = 'F'
                A_point = 'A'
                B_point = 'B'
                C_point = 'C'
                D_point = 'D'

                # Phần a
                mp_a1 = '(IBC)'
                mp_a2 = '(JAD)'
                gt_a = I_point + J_point
                mp_b1 = '(IBC)'
                mp_b2 = '(DMN)'
                gt_b = E_point + F_point
                # Nội dung câu hỏi
                noidungcauhoi = (f'''Cho tứ diện $ABCD$. Gọi $I, J$ lần lượt là trung điểm của $AD, BC$. $M$ là một điểm trên cạnh $AB$, $N$ là một điểm trên cạnh $AC$. \\\\
                a) Tìm giao tuyến của 2 mặt phẳng ${mp_a1}$ và ${mp_a2}$. \\\\
                b) Tìm giao tuyến của hai mặt phẳng ${mp_b1}$ và ${mp_b2}$.''')

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                           \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.7]
            \\clip(-2.0595325251671026,-2.902270879793007) rectangle (8.58760340453872,6.854856783342973);
            \\draw (0.,0.)-- (2.,6.);
            \\draw (2.,6.)-- (7.,0.);
            \\draw [dash pattern=on 1pt off 1pt] (7.,0.)-- (0.,0.);
            \\draw (0.,0.)-- (2.,-2.);
            \\draw (2.,-2.)-- (7.,0.);
            \\draw (2.,-2.)-- (2.,6.);
            \\draw (1.418,4.254)-- (2.,2.);
            \\draw (2.,2.)-- (7.,0.);
            \\draw (1,-1)-- (2,6);
            \\draw [dash pattern=on 1pt off 1pt](1,-1)-- (7,0);
            \\draw [dash pattern=on 1pt off 1pt] (1.418,4.254)-- (7.,0.);
            \\draw (4.5,3.)-- (2.,-2.);
            \\draw [dash pattern=on 1pt off 1pt] (1.,-1.)-- (4.5,3.);
            \\draw [dash pattern=on 1pt off 1pt] (4.5,3.)-- (0.,0.);
            \\draw [dash pattern=on 1pt off 1pt] (3.7,2.5)-- (3.7,1.3);
            \\draw (1.7806883287360815,6.7) node[anchor=north west] {$A$};
            \\draw (-0.79044666357678,0.4) node[anchor=north west] {$B$};
            \\draw (7.153701197287317,0.4) node[anchor=north west] {$D$};
            \\draw (1.3686474645833793,-1.9) node[anchor=north west] {$C$};
            \\draw (4.599047839540564,3.8) node[anchor=north west] {$I$};
            \\draw (0,-0.7) node[anchor=north west] {$J$};
            \\draw (1.2,2.2) node[anchor=north west] {$N$};
            \\draw (0.5775290054101911,4.7) node[anchor=north west] {$M$};
            \\draw (3.577186496441863,1.2) node[anchor=north west] {$E$};
            \\draw (3.42885178534689,3.35) node[anchor=north west] {$F$};
            \\end{tikzpicture}
                           \\end{center}'''
                    f'''a) Ta có: \\\\
                \\quad ${I_point} \\in {D_point}{A_point} \\Rightarrow {I_point} \\in {mp_a2}$. 
                \\quad ${I_point} \\in {mp_a1}$. \\\\
                \\quad ${J_point} \\in {B_point}{C_point} \\Rightarrow {J_point} \\in {mp_a1}$. \\\\
                \\quad ${J_point} \\in {mp_a2}$ (vì $J$ nằm trong mặt phẳng $(JAD)$). \\\\
                \\quad Vậy giao tuyến của hai mặt phẳng là ${{{mp_a1} \\cap {mp_a2} = {gt_a}}}$.\\\\'''

                f'''b) Trong mặt phẳng $({A_point}{B_point}{C_point})$, gọi ${E_point} = {M_point}{N_point} \\cap {B_point}{C_point}$. \\\\
                \\quad $\\Rightarrow {E_point} \\in {B_point}{C_point} \\Rightarrow {{{E_point} \\in {mp_b1}}}$. \\\\
                \\quad $\\Rightarrow {E_point} \\in {M_point}{N_point} \\Rightarrow {{{E_point} \\in {mp_b2}}}$. (1) \\\\
                Trong mặt phẳng $({A_point}{B_point}{D_point})$, gọi ${F_point} = {D_point}{M_point} \\cap {I_point}{B_point}$. \\\\
                \\quad $\\Rightarrow {F_point} \\in {I_point}{B_point} \\Rightarrow {{{F_point} \\in {mp_b1}}}$. \\\\
                \\quad $\\Rightarrow {F_point} \\in {D_point}{M_point} \\Rightarrow {{{F_point} \\in {mp_b2}}}$. (2) \\\\
                Từ (1) và (2), giao tuyến của hai mặt phẳng là đường thẳng đi qua ${E_point}$ và ${F_point}$. 
                ${{{mp_b1} \\cap {mp_b2} = {gt_b}}}$''')

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

