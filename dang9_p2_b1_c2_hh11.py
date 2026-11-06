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


def bt_dang9_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Bước 1: Khởi tạo biến và random số đo cạnh
            a_val = random.randint(2, 10)  # Random cạnh AB = AC = AD = a
            cd_sq = 2 * (a_val**2)
            cd_val_tex = latex(sqrt(cd_sq))

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho tứ diện $ABCD$ có $AB=AC=AD=%s$ và $\widehat{BAC}=\widehat{BAD}=60^\circ, \widehat{CAD}=90^\circ$. Gọi $I$ và $J$ lần lượt là trung điểm của $AB$ và $CD$.''' 
                             % (latex(a_val)))

            ########################################################################
            # Mệnh đề a: Tính CD
            ########################################################################
            da_a_d = '\\True $CD=%s$' % cd_val_tex
            da_a_s = '$CD=%s$' % latex(a_val)
            list_da_a = [da_a_d, da_a_s]
            chosen_a = random.choice(list_da_a)

            loigiai_a = ('''Xét tam giác $ACD$ vuông tại $A$ (do $\\widehat{CAD}=90^\\circ$), ta có:\\\\
                         $CD = \\sqrt{AC^2 + AD^2} = \\sqrt{%s^2 + %s^2} = %s$.''' 
                         % (latex(a_val), latex(a_val), cd_val_tex))

            ########################################################################
            # Mệnh đề b: Tính chất tam giác BCD
            ########################################################################
            da_b_d = 'Tam giác $BCD$ vuông cân tại $C$' # Sai, vì vuông tại B
            da_b_s = '\\True Tam giác $BCD$ vuông cân tại $B$'
            list_da_b = [da_b_d, da_b_s]
            chosen_b = random.choice(list_da_b)

            loigiai_b = ('''Xét các tam giác $ABC$ và $ABD$:\\\\
                         + Tam giác $ABC$ có $AB=AC=%s$ và $\\widehat{BAC}=60^\\circ$ nên là tam giác đều $\\Rightarrow BC=%s$.\\\\
                         + Tam giác $ABD$ có $AB=AD=%s$ và $\\widehat{BAD}=60^\\circ$ nên là tam giác đều $\\Rightarrow BD=%s$.\\\\
                         Xét tam giác $BCD$ có $BC^2 + BD^2 = %s^2 + %s^2 = %s$ và $CD^2 = (%s)^2 = %s$.\\\\
                         Vì $BC^2 + BD^2 = CD^2$ và $BC=BD$ nên tam giác $BCD$ vuông cân tại $B$.'''
                         % (latex(a_val), latex(a_val), latex(a_val), latex(a_val), 
                            latex(a_val), latex(a_val), latex(2*a_val**2), cd_val_tex, latex(2*a_val**2)))

            ########################################################################
            # Mệnh đề c: IJ vuông góc AB
            ########################################################################
            da_c_d = '\\True $IJ \\perp AB$'
            da_c_s = '$IJ$ không vuông góc với $AB$'
            list_da_c = [da_c_d, da_c_s]
            chosen_c = random.choice(list_da_c)

            loigiai_c = ('''Ta có $\\vec{IJ} = \\vec{AJ} - \\vec{AI} = \\frac{1}{2}(\\vec{AC} + \\vec{AD}) - \\frac{1}{2}\\vec{AB} = \\frac{1}{2}(\\vec{AC} + \\vec{AD} - \\vec{AB})$.\\\\
                         Xét tích vô hướng:\\\\
                         $\\vec{IJ} \\cdot \\vec{AB} = \\frac{1}{2}(\\vec{AC} \\cdot \\vec{AB} + \\vec{AD} \\cdot \\vec{AB} - AB^2)$\\\\
                         $= \\frac{1}{2}(%s \\cdot %s \\cdot \\cos 60^\\circ + %s \\cdot %s \\cdot \\cos 60^\\circ - %s^2) = \\frac{1}{2}(\\frac{%s}{2} + \\frac{%s}{2} - %s) = 0$.\\\\
                         Vậy $IJ \\perp AB$.'''
                         % (latex(a_val), latex(a_val), latex(a_val), latex(a_val), latex(a_val), 
                            latex(a_val**2), latex(a_val**2), latex(a_val**2)))

            ########################################################################
            # Mệnh đề d: IJ vuông góc CD
            ########################################################################
            da_d_d = '\\True $IJ \\perp CD$'
            da_d_s = '$IJ$ không vuông góc với $CD$'
            list_da_d = [da_d_d, da_d_s]
            chosen_d = random.choice(list_da_d)

            loigiai_d = ('''Ta có $\\vec{CD} = \\vec{AD} - \\vec{AC}$.\\\\
                         Xét tích vô hướng:\\\\
                         $\\vec{IJ} \\cdot \\vec{CD} = \\frac{1}{2}(\\vec{AC} + \\vec{AD} - \\vec{AB}) \\cdot (\\vec{AD} - \\vec{AC})$\\\\
                         $= \\frac{1}{2}(AD^2 - AC^2 - \\vec{AB} \\cdot \\vec{AD} + \\vec{AB} \\cdot \\vec{AC})$\\\\
                         $= \\frac{1}{2}(%s^2 - %s^2 - %s^2 \\cos 60^\\circ + %s^2 \\cos 60^\\circ) = 0$.\\\\
                         Vậy $IJ \\perp CD$.'''
                         % (latex(a_val), latex(a_val), latex(a_val), latex(a_val)))

            # Hình vẽ TikZ
            hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round]
                \coordinate (A) at (0,3);
                \coordinate (B) at (-1.5,-0.5);
                \coordinate (C) at (0.5,-1.5);
                \coordinate (D) at (2.5,0);
                \coordinate (I) at ($(A)!0.5!(B)$);
                \coordinate (J) at ($(C)!0.5!(D)$);
                \draw[dashed] (B)--(D) (I)--(J);
                \draw (A)--(B)--(C)--(D)--(A)--(C);
                \foreach \p/\pos in {A/above, B/left, C/below, D/right, I/left, J/right}
                    \fill (\p) node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}'''

            # Tổng hợp nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                str(hinh_ve) + 
                '\\choiceTFn \n'
                '{' + str(chosen_a) + '}\n'
                '{' + str(chosen_b) + '}\n'
                '{' + str(chosen_c) + '}\n'
                '{' + str(chosen_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

