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


def bt_dang10_p4_b2_c2_hh11(self):
            # Khai báo biến
            # Ta sẽ random tên các đỉnh của hình chữ nhật và các điểm hình chiếu
            ds_dinh_day = [('A', 'B', 'C', 'D'),]
            dinh_chon = random.choice(ds_dinh_day)
            A, B, C, D = dinh_chon

            ds_hinh_chieu = [('H', 'K'),]
            hc_chon = random.choice(ds_hinh_chieu)
            H, K = hc_chon

            S = 'S'

            # B2: Viết lại bài toán và lời giải theo mẫu
            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $' + S + '.' + A + B + C + D + '$ có đáy $' + A + B + C + D + '$ là hình chữ nhật, cạnh bên $' + S + A + '$ vuông góc với đáy. '
                'Gọi $' + H + '$, $' + K + '$ lần lượt là hình chiếu của $' + A + '$ lên $' + S + C + '$, $' + S + D + '$. Chứng minh $' + A + K + ' \\perp (' + S + C + D + ')$.'
            )

            # Các phương án
            da_dung = '\\True $' + A + K + ' \\perp (' + S + C + D + ')$'
            da_sai1 = '$' + A + H + ' \\perp (' + S + C + D + ')$'
            da_sai2 = '$' + B + D + ' \\perp (' + S + A + C + ')$'
            da_sai3 = '$' + B + C + ' \\perp (' + S + A + C + ')$'

            # Trộn đáp án (B4)
            list_1 = [da_dung, da_sai1, da_sai2, da_sai3]
            random.shuffle(list_1)


            # Lời giải chi tiết
            loigiai = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (131.47,128.4) -- (251.47,128.4) ;
            		\draw [line width=1]    (91.47,168.4) -- (211.47,168.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (91.47,168.4) -- (131.47,128.4) ;
            		\draw [line width=1]    (211.47,168.4) -- (251.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (131.47,128.4) -- (131.47,48.4) ;
            		\draw [line width=1]    (91.47,168.4) -- (131.47,48.4) ;
            		\draw [line width=1]    (251.47,128.4) -- (131.47,48.4) ;
            		\draw [line width=1]    (211.47,168.4) -- (131.47,48.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (174.47,77.4) -- (131.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (150.47,78.4) -- (131.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (131.47,128.4) -- (211.47,168.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (91.47,168.4) -- (251.47,128.4) ;
            		\draw (124,26) node [anchor=north west][inner sep=0.75pt]    {$S$};
            		\draw (124.47,130.4) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (77,168) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (211.47,168.4) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (131,68) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\draw (175,54) node [anchor=north west][inner sep=0.75pt]    {$K$};
            		\draw (254,112) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\end{tikzpicture}
            \end{center}'''
                'Ta có $' + C + D + ' \\perp ' + A + D + '$ (do $' + A + B + C + D + '$ là hình chữ nhật) và '
                '$' + C + D + ' \\perp ' + S + A + '$ (do $' + S + A + ' \\perp (' + A + B + C + D + ')$). \\\\'
                'Suy ra $' + C + D + ' \\perp (' + S + A + D + ')$. \\\\'
                'Mà $' + A + K + ' \\subset (' + S + A + D + ')$ nên $' + C + D + ' \\perp ' + A + K + '$. \\\\'
                'Mặt khác, theo giả thiết ta có $' + A + K + ' \\perp ' + S + D + '$. \\\\'
                'Vì $' + A + K + '$ vuông góc với hai đường thẳng cắt nhau $' + C + D + '$ và $' + S + D + '$ trong mặt phẳng $(' + S + C + D + ')$, '
                'nên $' + A + K + ' \\perp (' + S + C + D + ')$.'
            )

            # Xuất nội dung theo cấu trúc mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n' 
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

