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


def bt_dang7_p4_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        list_diem = ['A', 'B', 'C', 'D', 'M', 'N', 'P', 'Q', 'E', 'F']
        random.shuffle(list_diem)
        D1 = list_diem[0]
        D2 = list_diem[1]
        D3 = list_diem[2]
        D4 = list_diem[3]
        D_chung = list_diem[4]
        S = 'S'
        noidungcauhoi = f"Cho hình chóp ${S}.{D1}{D2}{D3}{D4}$ có đáy ${D1}{D2}{D3}{D4}$ là hình bình hành. Chứng minh rằng ${D1}{D2} \\parallel ({S}{D3}{D4})$"
        loigiai = f'''\\begin{{center}}
    \\begin{{tikzpicture}}[scale=1, line join=round, line cap=round]
    \\def\\a{{2}} \\def\\b{{1.5}} \\def\\h{{3}}
    \\coordinate ({D1}) at (0,0);
    \\coordinate ({D2}) at (\\a,\\b);
    \\coordinate ({D4}) at (\\a+2,0);
    \\coordinate ({D3}) at ($({D4})-({D1})+({D2})$);
    \\coordinate ({S}) at (1,3);
    \\draw[dashed] ({D1}) -- ({D2}) -- ({D3});
    \\draw[dashed] ({D1}) -- ({S}) -- ({D2});
    \\draw ({D1}) -- ({D4}) -- ({D3}) -- ({S}) -- ({D4});
    \\draw ({S}) -- ({D1});
    \\tkzDrawPoints({S},{D1},{D2},{D3},{D4})
    \\tkzLabelPoints[above]({S})
    \\tkzLabelPoints[left]({D1},{D4})
    \\tkzLabelPoints[right]({D2},{D3})
    \\end{{tikzpicture}}
    \\end{{center}}
    Nếu đường thẳng ${D1}{D2}$ và mặt phẳng $({S}{D3}{D4})$ có điểm chung là ${D_chung}$ thì điểm ${D_chung}$ nằm trên cả hai mặt phẳng $({D1}{D2}{D3}{D4})$ và $({S}{D3}{D4})$ suy ra điểm ${D_chung}$ nằm trên ${D3}{D4}$. \\\\
    Do đó ${D_chung}$ là điểm chung của hai đường thẳng ${D1}{D2}$ và ${D3}{D4}$. \\\\
    Điều này không xảy ra vì ${D1}{D2} \\parallel {D3}{D4}$. \\\\
    Vậy ${D1}{D2} \\parallel ({S}{D3}{D4})$.
    '''
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content  

