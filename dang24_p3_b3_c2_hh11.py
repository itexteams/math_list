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


def bt_dang24_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo danh sách dạng bài
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 & B3: Thiết lập thông số ngẫu nhiên
                # Cạnh của hình chóp đều
                a_val = random.randint(2, 12)

                # Tính toán các giá trị hình học (S.ABCD có tất cả các cạnh bằng a)
                # AC = a*sqrt(2), AO = AC/2 = a*sqrt(2)/2
                # cos(SAO) = AO/SA = (a*sqrt(2)/2)/a = sqrt(2)/2 => Góc = 45 độ
                goc_kq = 45

                # B4: Thiết lập đáp án đúng và các phương án sai
                da = r'%s^\circ' % (goc_kq)

                # Danh sách các phương án sai (không chứa 45)
                s = [r'30^\circ', r'60^\circ', r'90^\circ', r'15^\circ', r'75^\circ', r'120^\circ']
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = (r'Cho hình chóp $S.ABCD$ có tất cả các cạnh đều bằng $%s$. Gọi $E, F$ lần lượt là trung điểm của $SB$ và $SD$, $O$ là giao điểm của $AC$ và $BD$. Góc giữa đường thẳng $SA$ và mặt phẳng $\left(ABCD\right)$ bằng bao nhiêu?'
                                 % (latex(a_val)))

                # Các đáp án trắc nghiệm
                da_d = r'\True $%s$' % (da)
                da_s1 = r'$%s$' % (das1)
                da_s2 = r'$%s$' % (das2)
                da_s3 = r'$%s$' % (das3)

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Thiết lập hình vẽ TikZ
                tikz_code = ('\\begin{center}'
                    '\\begin{tikzpicture}[line width=1pt, scale=0.8]\n'
                    '\\coordinate (A) at (1,2);\n'
                    '\\coordinate (B) at (-1,0);\n'
                    '\\coordinate (C) at (2.5,0);\n'
                    '\\coordinate (D) at (4.5,2);\n'
                    '\\coordinate (O) at (2.125,1);\n'
                    '\\coordinate (S) at (2.125,5);\n'
                    '\\coordinate (E) at ($(S)!0.5!(B)$);\n'
                    '\\coordinate (F) at ($(S)!0.5!(D)$);\n'
                    '\\draw[dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (E)--(F);\n'
                    '\\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);\n'
                    '\\node[above] at (S) {$S$};\n'
                    '\\node[left] at (A) {$A$};\n'
                    '\\node[left] at (B) {$B$};\n'
                    '\\node[below] at (C) {$C$};\n'
                    '\\node[right] at (D) {$D$};\n'
                    '\\node[below] at (O) {$O$};\n'
                    '\\node[left] at (E) {$E$};\n'
                    '\\node[right] at (F) {$F$};\n'
                    '\\foreach \\p in {S,A,B,C,D,O,E,F} \\fill (\\p) circle (1.5pt);\n'
                    '\\end{tikzpicture}'
                    '\\end{center}'
            )

                # Nội dung lời giải chi tiết
                loigiai = (r'''%s 
            Ta có: \\
            + $S.ABCD$ là hình chóp đều có tất cả các cạnh bằng $a = %s$. \\
            + Vì $S.ABCD$ là hình chóp đều nên $SO \perp (ABCD)$ (với $O$ là tâm của đáy $ABCD$). \\
            + Khi đó, hình chiếu của $SA$ lên mặt phẳng $(ABCD)$ là $AO$. \\
            + Suy ra $\left(SA, (ABCD)\right) = \widehat{SAO}$. \\
            + Xét hình vuông $ABCD$ cạnh $a = %s$, ta có đường chéo $AC = a\sqrt{2} = %s\sqrt{2}$. \\
            + Suy ra $AO = \frac{AC}{2} = \frac{%s\sqrt{2}}{2}$. \\
            + Xét tam giác $SAO$ vuông tại $O$, ta có: \\
            $\cos \widehat{SAO} = \frac{AO}{SA} = \frac{\frac{%s\sqrt{2}}{2}}{%s} = \frac{\sqrt{2}}{2}$. \\
            $\Rightarrow \widehat{SAO} = 45^\circ$.''' 
                           % (tikz_code, latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(45))

            # Xuất câu trắc nghiệm theo mẫu content
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

