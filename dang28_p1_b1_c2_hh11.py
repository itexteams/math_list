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


def bt_dang28_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lis_a = [1, 2, 3, 4, 5] # Các hệ số có thể random cho cạnh a
            k = random.choice(lis_a)
            if k == 1:
                canh_str = "a"
            else:
                canh_str = f"{k}a"

            # Tính toán logic (Góc luôn là 120 độ trong trường hợp OA=OB=OC)
            # Tuy nhiên ta random các đáp án sai xung quanh các giá trị góc đặc biệt
            kq_dung = 120
            list_sai = [60, 135, 150, 45, 90]
            random.shuffle(list_sai)

            # Chọn 3 đáp án sai
            das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $O.ABC$ có ba cạnh $OA, OB, OC$ đôi một vuông góc và $OA = OB = OC = %s$. Gọi $M$ là trung điểm cạnh $AB$. Góc hợp bởi hai vectơ $\\overrightarrow{BC}$ và $\\overrightarrow{OM}$ bằng'''
                            % (canh_str))

            # Các đáp án
            da_d = ('\\True $%s^\\circ$' % (kq_dung))
            da_s1 = ('$%s^\\circ$' % (das1))
            da_s2 = ('$%s^\\circ$' % (das2))
            da_s3 = ('$%s^\\circ$' % (das3))

            # Trộn đáp án
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Hình vẽ TikZ
            tikz_code = r'''
            \begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw [line width=1]    (89.47,40.07) -- (90,143) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (90,143) -- (201.47,143.07) ;
            	\draw [line width=1]    (90,143) -- (141.47,186.07) ;
            	\draw [line width=1]    (201.47,143.07) -- (141.47,186.07) ;
            	\draw [line width=1]    (89.47,40.07) -- (141.47,186.07) ;
            	\draw [line width=1]    (89.47,40.07) -- (201.47,143.07) ; 
            	\draw [line width=1]    (121.47,132.07) -- (90,143) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (136.47,85.07) -- (90,143) ;
            	\draw [line width=1]    (136.47,85.07) -- (121.47,132.07) ;
            	\draw (75,17) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (203,133) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (134,187) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (68,135) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (126,120) node [anchor=north west][inner sep=0.75pt]    {$I$};
            	\draw (133,61) node [anchor=north west][inner sep=0.75pt]    {$M$};
            \end{tikzpicture}
            \end{center}'''

            # Nội dung lời giải chi tiết
            loigiai = ('''Gọi $I$ là trung điểm của $AC$. Trong tam giác $ABC$, $MI$ là đường trung bình nên $MI \\parallel BC$ và $MI = \\frac{1}{2}BC$. \\\\
                      Ta có $\\overrightarrow{BC} = 2\\overrightarrow{MI}$, do đó góc giữa $(\\overrightarrow{BC}, \\overrightarrow{OM})$ chính bằng góc giữa $(\\overrightarrow{MI}, \\overrightarrow{OM})$. \\\\
                      Xét các tam giác vuông cân $OAB, OBC, OAC$ tại $O$ có cạnh góc vuông bằng $%s$: \\\\
                      $BC = \\sqrt{OB^2 + OC^2} = %s\\sqrt{2} \\Rightarrow MI = \\frac{%s\\sqrt{2}}{2}$. \\\\
                      $OM$ là đường trung tuyến của tam giác vuông cân $OAB$ nên $OM = \\frac{AB}{2} = \\frac{%s\\sqrt{2}}{2}$. \\\\
                      $OI$ là đường trung tuyến của tam giác vuông cân $OAC$ nên $OI = \\frac{AC}{2} = \\frac{%s\\sqrt{2}}{2}$. \\\\
                      Suy ra $MI = OM = OI = \\frac{%s\\sqrt{2}}{2}$, hay tam giác $OMI$ đều. \\\\
                      Khi đó $\\widehat{OMI} = 60^\\circ$. \\\\
                      Ta có $(\\overrightarrow{MI}, \\overrightarrow{MO}) = \\widehat{OMI} = 60^\\circ$. \\\\
                      Do đó $(\\overrightarrow{BC}, \\overrightarrow{OM}) = (\\overrightarrow{MI}, \\overrightarrow{OM}) = 180^\\circ - (\\overrightarrow{MI}, \\overrightarrow{MO}) = 180^\\circ - 60^\\circ = 120^\\circ$.''' 
                      % (canh_str, canh_str, canh_str, canh_str, canh_str, canh_str))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + tikz_code +
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

