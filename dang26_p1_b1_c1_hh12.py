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


def bt_dang26_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Define problem type, although for this problem it's static
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- vectơ equations for the problem ---
                # True statements (distractors)
                du = [
                    r'$\vec{GA} + \vec{GB} + \vec{GC} + \vec{GD} = \vec{0}$',
                    r'$\vec{AD} + \vec{BC} = 2\vec{MN}$',
                    r'$\vec{AC} + \vec{BD} = 2\vec{MN}$',
                    r'$\vec{AD} + \vec{BC} = \vec{AC} + \vec{BD}$'
                ]

                # False statements (the correct answer)
                da = [
                    r'$\vec{AD} + \vec{BC} = \vec{MN}$',
                    r'$\vec{AC} + \vec{BD} = \vec{AD} + \vec{CB}$',
                    r'$\vec{GA} + \vec{GB} = \vec{GC} + \vec{GD}$',
                    r'$\vec{AB} + \vec{CD} = \vec{AC} + \vec{BD}$'
                ]

                # Select the correct answer and three incorrect distractors
                correct_answer = random.choice(da)
                da.remove(correct_answer)
                distractors = random.sample(du, 3)

                # --- Question and Solution Content ---
                noidungcauhoi = ('''Cho tứ diện $ABCD$, hai điểm $M, N$ lần lượt là trung điểm của $AB, CD$. Điểm $G$ là trung điểm của đoạn thẳng $MN$. Phát biểu nào sau đây sai?'''
                )

                # The solution explains why the true statements are correct,
                # thereby showing why any other statement is false.
                loigiai = ('''Ta có $M$ là trung điểm $AB$ và $N$ là trung điểm $CD$. $G$ là trung điểm $MN$. \\\\
                Sử dụng quy tắc ba điểm, ta có: \\\\
                $\\vec{GA} + \\vec{GB} = 2\\vec{GM}$ và $\\vec{GC} + \\vec{GD} = 2\\vec{GN}$. \\\\
                Do đó, $\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = 2(\\vec{GM} + \\vec{GN})$. Vì $G$ là trung điểm $MN$, nên $\\vec{GM} + \\vec{GN} = \\vec{0}$. \\\\
                Suy ra $\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$.\\\\
                $\\vec{AD} = \\vec{AM} + \\vec{MN} + \\vec{ND}$ và $\\vec{BC} = \\vec{BM} + \\vec{MN} + \\vec{NC}$.\\\\
                Do đó, $\\vec{AD} + \\vec{BC} = (\\vec{AM} + \\vec{BM}) + (\\vec{ND} + \\vec{NC}) + 2\\vec{MN}$.\\\\
                Vì $M$ là trung điểm $AB$ và $N$ là trung điểm $CD$, ta có $\\vec{AM} + \\vec{BM} = \\vec{0}$ và $\\vec{ND} + \\vec{NC} = \\vec{0}$.\\\\
                Vậy $\\vec{AD} + \\vec{BC} = 2\\vec{MN}$.\\\\
                Tương tự, $\\vec{AC} = \\vec{AM} + \\vec{MN} + \\vec{NC}$ và $\\vec{BD} = \\vec{BM} + \\vec{MN} + \\vec{ND}$.\\\\
                Do đó, $\\vec{AC} + \\vec{BD} = (\\vec{AM} + \\vec{BM}) + (\\vec{NC} + \\vec{ND}) + 2\\vec{MN}$.\\\\
                Vậy $\\vec{AC} + \\vec{BD} = 2\\vec{MN}$.\\\\
                Từ hai kết quả trên, ta có $\\vec{AD} + \\vec{BC} = \\vec{AC} + \\vec{BD}$.\\\\
                Các phát biểu trên đều đúng. Phát biểu sai là: ''' + correct_answer)

                # Prepare answers for output
                list_1 = [
                    '\\True ' + correct_answer,
                    distractors[0],
                    distractors[1],
                    distractors[2]
                ]

                random.shuffle(list_1)

                # --- Print the LaTeX content ---
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) +
                           '\\choice \n'
                           '{' + str(list_1[1]) + '}\n'
                           '{' + str(list_1[2]) + '}\n'
                           '{' + str(list_1[3]) + '}\n'
                           '{' + str(list_1[0]) + '}\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

