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


def bt_dang25_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Đáy AD // BC, I = AB cap CD
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình thang $ABCD$ ($AD // BC$). Gọi $I$ là giao điểm của $AB$ và $DC$, $M$ là trung điểm $SC$. $DM$ cắt mặt phẳng $(SAB)$ tại $J$. Khẳng định nào sau đây sai?''')

        da_sai = '$JM \\subset mp(SAB)$'
        da_dung_1 = '$S, I, J$ thẳng hàng'
        da_dung_2 = '$DM \\subset mp(SCI)$'
        da_dung_3 = '$SI = (SAB) \\cap (SCD)$'

        # Đánh dấu \True vào khẳng định sai (vì đề hỏi khẳng định SAI)
        da_d = ('\\True ' + str(da_sai))
        da_s1 = str(da_dung_1)
        da_s2 = str(da_dung_2)
        da_s3 = str(da_dung_3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Ta xét từng khẳng định:\\\\
    - Ta có $I = AB \\cap CD \\Rightarrow I \\in AB \\subset (SAB)$ và $I \\in CD \\subset (SCD)$.\\\\
    Do đó $(SAB) \\cap (SCD) = SI$. Vậy khẳng định $SI = (SAB) \\cap (SCD)$ là đúng.\\\\
    - Vì $J = DM \\cap (SAB) \\Rightarrow J \\in (SAB)$.\\\\
    Mặt khác $DM \\subset (SCD)$ nên $J \\in (SCD)$.\\\\
    Suy ra $J \\in (SAB) \\cap (SCD) = SI$, hay $S, I, J$ thẳng hàng. Vậy khẳng định $S, I, J$ thẳng hàng là đúng.\\\\
    - Lại có $M \\in SC \\subset (SCI)$ và $D \\in CD \\subset (SCI) \\Rightarrow DM \\subset mp(SCI)$. Vậy khẳng định $DM \\subset mp(SCI)$ là đúng.\\\\
    - Do $M \\notin (SAB)$ nên đường thẳng $JM$ không thể nằm trong mặt phẳng $(SAB)$. Vậy khẳng định $JM \\subset mp(SAB)$ là sai.''')

    elif dang == '2':
        # Dạng 2: Đáy AB // CD, I = AD cap BC
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình thang $ABCD$ ($AB // CD$). Gọi $I$ là giao điểm của $AD$ và $BC$, $M$ là trung điểm $SD$. $CM$ cắt mặt phẳng $(SAB)$ tại $J$. Khẳng định nào sau đây sai?''')

        da_sai = '$JM \\subset mp(SAB)$'
        da_dung_1 = '$S, I, J$ thẳng hàng'
        da_dung_2 = '$CM \\subset mp(SDI)$'
        da_dung_3 = '$SI = (SAD) \\cap (SBC)$'

        da_d = ('\\True ' + str(da_sai))
        da_s1 = str(da_dung_1)
        da_s2 = str(da_dung_2)
        da_s3 = str(da_dung_3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Ta xét từng khẳng định:\\\\
    - Ta có $I = AD \\cap BC \\Rightarrow I \\in AD \\subset (SAD)$ và $I \\in BC \\subset (SBC)$.\\\\
    Do đó $(SAD) \\cap (SBC) = SI$. Vậy khẳng định $SI = (SAD) \\cap (SBC)$ là đúng.\\\\
    - Vì $J = CM \\cap (SAB) \\Rightarrow J \\in (SAB)$.\\\\
    Mặt khác $CM \\subset (SCD)$ nên $J \\in (SCD)$.\\\\
    Lại có $I = AD \\cap BC \\Rightarrow I \\in (SAB) \\cap (SCD) = SI$.\\\\
    Suy ra $J \\in SI$, hay $S, I, J$ thẳng hàng. Vậy khẳng định $S, I, J$ thẳng hàng là đúng.\\\\
    - Lại có $M \\in SD \\subset (SDI)$ và $C \\in BC \\subset (SDI) \\Rightarrow CM \\subset mp(SDI)$. Vậy khẳng định $CM \\subset mp(SDI)$ là đúng.\\\\
    - Do $M \\notin (SAB)$ nên đường thẳng $JM$ không thể nằm trong mặt phẳng $(SAB)$ là sai.''')

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

