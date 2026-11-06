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


def bt_dang11_p2_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$ và tam giác $ABC$ vuông tại $B$. Gọi $H, K$ là hình chiếu vuông góc của $A$ trên các cạnh $SB, SC$.'''
                             '\n\\begin{center}\n'
                             '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, line width=1pt]\n'
                             '\\coordinate (A) at (0,0);\n'
                             '\\coordinate (B) at (1.2,-1.2);\n'
                             '\\coordinate (C) at (4,0);\n'
                             '\\coordinate (S) at (0,3);\n'
                             '\\coordinate (H) at ($(S)!0.55!(B)$);\n'
                             '\\coordinate (K) at ($(S)!0.65!(C)$);\n'
                             '\\draw (S)--(A) (A)--(H) (S)--(B) (S)--(C) (A)--(B) (B)--(C) (H)--(K);\n'
                             '\\draw[dashed] (A)--(C)  (A)--(K) ;\n'
                             '\\draw (0,0.2)--(0.2,0.2)--(0.2,0); % Goc vuong tai A\n'
                             '\\draw (1.05,-1.05)--(1.2,-0.9)--(1.35,-1.05); % Goc vuong tai B\n'
                             '\\node[left] at (A) {$A$};\\node[below] at (B) {$B$};\\node[right] at (C) {$C$};\\node[above] at (S) {$S$};\n'
                             '\\node[left] at (H) {$H$};\\node[right] at (K) {$K$};\n'
                             '\\end{tikzpicture}\n'
                             '\\end{center}\n' )

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tam giác $SBC$ vuông tại $B$'
            nb_da_1_s = 'Tam giác $SBC$ cân tại $B$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $BC \\perp AB$ (do tam giác $ABC$ vuông tại $B$) và $BC \\perp SA$ (do $SA \\perp (ABC)$). \\\\
                            Suy ra $BC \\perp (SAB)$. Mà $SB \\subset (SAB)$, nên $BC \\perp SB$. \\\\
                            Vậy tam giác $SBC$ vuông tại $B$. Mệnh đề cho rằng tam giác $SBC$ cân tại $B$ là sai.''')

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $AH$ vuông góc với mặt phẳng $(SBC)$'
            th_da_1_s = '$AH$ vuông góc với mặt phẳng $(SAC)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Nội dung lời giải
            loigiai_th_1 = ('''Vì $BC \\perp (SAB)$ và $AH \\subset (SAB)$ nên $AH \\perp BC$. \\\\
                            Theo giả thiết, $H$ là hình chiếu của $A$ lên $SB$ nên $AH \\perp SB$. \\\\
                            Ta có $\\left\\{ \\begin{array}{l} AH \\perp SB \\\\ AH \\perp BC \\end{array} \\right. \\Rightarrow AH \\perp (SBC)$.''')

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $(SC, HK) = 90^\\circ$'
            vd_da_1_s = '$(SC, HK) = 45^\\circ$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $AH \\perp (SBC) \\Rightarrow AH \\perp SC$ (vì $SC \\subset (SBC)$). \\\\
                            Theo giả thiết, $K$ là hình chiếu của $A$ lên $SC$ nên $AK \\perp SC$. \\\\
                            Từ đó suy ra $SC \\perp (AHK)$. Vì $HK \\subset (AHK)$ nên $SC \\perp HK$. \\\\
                            Vậy góc giữa $SC$ và $HK$ bằng $90^\\circ$.''')

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Giả sử $HK$ cắt $BC$ tại $D$. Khi đó $(AC, AD) = 90^\\circ$'
            vdc_da_1_s = 'Giả sử $HK$ cắt $BC$ tại $D$. Khi đó $(AC, AD) = 60^\\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Vì $SC \\perp (AHK)$ và $D \\in HK \\subset (AHK)$ nên $SC \\perp AD$. (1) \\\\
                             Mặt khác, $SA \\perp (ABC)$ và $AD \\subset (ABC)$ nên $SA \\perp AD$. (2) \\\\
                             Từ (1) và (2) suy ra $AD \\perp (SAC)$. \\\\
                             Mà $AC \\subset (SAC)$, do đó $AD \\perp AC$. \\\\
                             Vậy góc giữa $AC$ và $AD$ bằng $90^\\circ$.''')

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào danh sách để xuất content
            list_nb_1 = [nb_da_1]; list_nb_2 = [loigiai_nb_1]
            list_th_1 = [th_da_1]; list_th_2 = [loigiai_th_1]
            list_vd_1 = [vd_da_1]; list_vd_2 = [loigiai_vd_1]
            list_vdc_1 = [vdc_da_1]; list_vdc_2 = [loigiai_vdc_1]

            # Xuất câu hỏi với đáp án và lời giải (giữ nguyên thứ tự a, b, c, d như đề bài)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

