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


def bt_dang10_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo các ký hiệu điểm để có thể thay đổi nếu muốn random tên đỉnh
            A, B, C, O, K, H = 'A', 'B', 'C', 'O', 'K', 'H'

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$ có $%s%s, %s%s, %s%s$ đôi một vuông góc với nhau. Gọi $%s%s$ là đường cao của tam giác $%s%s%s$ và $%s%s$ là đường cao của tam giác $%s%s%s$.''' 
                             %(O, A, B, C, O, A, O, B, O, C, O, K, O, B, C, O, H, O, A, K))

            # Hình vẽ TikZ giống 100% cấu trúc hình học không gian
            hinh_ve = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (278.32,139.69) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (103.47,30.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (48.47,189.4) ;
            		\draw [line width=1]    (48.47,189.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (278.32,139.69) ;
            		\draw [line width=1]    (103.47,30.4) -- (48.47,189.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (103.47,139.69) -- (163.4,164.54) ;
            		\draw [line width=1]    (103.47,30.4) -- (163.4,164.54) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (133.43,97.47) -- (103.47,139.69) ;
            		\draw (83,120) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (35,191) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (283,128) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (95,5) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (137,79) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\draw (163.4,164.54) node [anchor=north west][inner sep=0.75pt]    {$K$};
            	\end{tikzpicture}
            \end{center}''')

            ########################################################################
            # Nhận biết
            nb_da_1_d = '\\True $%s%s \\perp (%s%s%s)$' % (O, A, O, B, C)
            nb_da_1_s = '$%s%s \\perp (%s%s%s)$' % (O, B, O, A, K)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Vì $%s%s \\perp %s%s$ và $%s%s \\perp %s%s$ nên $%s%s \\perp (%s%s%s)$.'''
                            % (O, A, O, B, O, A, O, C, O, A, O, B, C))

            ########################################################################
            # Thông hiểu
            th_da_1_d = '\\True $%s%s \\perp (%s%s%s)$' % (O, B, O, A, C)
            th_da_1_s = '$%s%s \\perp (%s%s%s)$' % (O, B, A, B, C)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Tương tự câu a, ta có $%s%s \\perp %s%s$ và $%s%s \\perp %s%s$ nên $%s%s \\perp (%s%s%s)$.'''
                            % (O, B, O, A, O, B, O, C, O, B, O, A, C))

            ########################################################################
            # Vận dụng
            vd_da_1_d = '\\True Các cạnh đối nhau trong tứ diện $%s%s%s%s$ thì vuông góc với nhau' % (O, A, B, C)
            vd_da_1_s = 'Các cạnh đối nhau trong tứ diện $%s%s%s%s$ thì không vuông góc với nhau' % (O, A, B, C)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Ta có $%s%s \\perp (%s%s%s) \\Rightarrow %s%s \\perp %s%s$. Tương tự $%s%s \\perp %s%s$ và $%s%s \\perp %s%s$. Vậy các cặp cạnh đối diện vuông góc.'''
                            % (O, A, O, B, C, O, A, B, C, O, B, A, C, O, C, A, B))

            ########################################################################
            # Vận dụng cao
            vdc_da_1_d = '$%s%s$ không vuông góc với mặt phẳng $(%s%s%s)$' % (O, H, A, B, C)
            vdc_da_1_s = '\\True $%s%s \\perp (%s%s%s)$' % (O, H, A, B, C)
            # Lưu ý: Trong ảnh mệnh đề (d) là "không vuông góc" -> Sai. Nên vdc_da_1_d ở đây đại diện cho phát biểu Sai.
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Ta có $%s%s \\perp %s%s$ và $%s%s \\perp %s%s$ (do $%s%s \\perp (%s%s%s)$) nên $%s%s \\perp (%s%s%s) \\Rightarrow %s%s \\perp %s%s$. \\\\ Mà $%s%s \\perp %s%s$, suy ra $%s%s \\perp (%s%s%s)$.'''
                             % (B, C, O, K, B, C, O, A, O, A, O, B, C, B, C, O, A, K, B, C, O, H, O, H, A, K, O, H, A, B, C))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi chọn được bộ đáp án thỏa mãn (1-3 câu đúng)
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + 
                '\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                +str(hinh_ve)+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

