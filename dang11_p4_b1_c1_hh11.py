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


def bt_dang11_p4_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':


                # Nội dung câu hỏi
                noidungcauhoi =  ('''Cho hình chóp $S.ABCD$, có đáy là hình thang, cạnh đáy lớn $AB$. Gọi $I, J, K$ là ba điểm lần lượt trên $SA, AB, BC$.\\\\
            a) Tìm giao điểm của đường thẳng $IK$ và mặt phẳng $(SBD)$.\\\\
            b) Tìm giao điểm của mặt phẳng $(IJK)$ với $SD$.'''
                )

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                           \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,scale=0.7]
            	\\clip(-1.7267018220232515,-2.844414689392874) rectangle (9.505740904565634,4.833035019716902);
            	\\draw [dash pattern=on 1pt off 1pt] (0.,0.)-- (6.,0.);
            	\\draw (6.,0.)-- (4.2,-2.);
            	\\draw (4.2,-2.)-- (2.,-2.);
            	\\draw (2.,-2.)-- (0.,0.);
            	\\draw (3.,4.)-- (0.,0.);
            	\\draw (2.,-2.)-- (3.,4.);
            	\\draw (3.,4.)-- (4.2,-2.);
            	\\draw (6.,0.)-- (3.,4.);
            	\\draw [dash pattern=on 1pt off 1pt] (0.,0.)-- (4.2,-2.);
            	\\draw [dash pattern=on 1pt off 1pt] (1.,-1.)-- (6.,0.);
            	\\draw [dash pattern=on 1pt off 1pt] (1.,-1.)-- (4.5,2.);
            	\\draw (3.4390243902439024,1.8048780487804879)-- (8.454545454545455,2.727272727272727);
            	\\draw [dash pattern=on 1pt off 1pt] (8.454545454545455,2.727272727272727)-- (1.,-1.);
            	\\draw (6.,0.)-- (8.454545454545455,2.727272727272727);
            	\\draw [dash pattern=on 1pt off 1pt] (3.,4.)-- (1.774647887323944,-0.8450704225352114);
            	\\draw (5.9,0.39346627488385766) node[anchor=north west] {$A$};
            	\\draw (-0.6752250140364763,0.49360692326355043) node[anchor=north west] {$B$};
            	\\draw (1.4,-1.8930785297857928) node[anchor=north west] {$C$};
            	\\draw (4,-1.8430082055959465) node[anchor=north west] {$D$};
            	\\draw (2.8630778953793388,4.8664152358434665) node[anchor=north west] {$S$};
            	\\draw (1.2,0.3767761668205756) node[anchor=north west] {$T$};
            	\\draw (1.34,-0.7247709653560445) node[anchor=north west] {$M$};
            	\\draw (0.1,-0.8082215056724551) node[anchor=north west] {$K$};
            	\\draw (2.6,0.8) node[anchor=north west] {$J$};
            	\\draw (4.4,2.7968418359964833) node[anchor=north west] {$I$};
            	\\draw (2.6,2.2460682699081733) node[anchor=north west] {$Q$};
            	\\draw (8.771376149781219,3.197404429515254) node[anchor=north west] {$P$};
            \\end{tikzpicture}
                           \\end{center}'''
                    '''a) Tìm giao điểm $T$ của $IK$ và mặt phẳng $(SBD)$\\\\
                    Chọn $\\text{mp}(SAK)$ chứa đường thẳng $IK$.\\\\
                Tìm giao tuyến $SM$ của $\\text{mp}(SAK)$ và $\\text{mp}(SBD)$.\\\\
                    Trong $\\text{mp}(ABCD)$, gọi $M = AK \\cap BD$.\\\\
                    Giao tuyến là đường thẳng $SM$ (vì $S$ và $M$ là hai điểm chung).\\\\
                    Trong $\\text{mp}(SAK)$, gọi $T = IK \\cap SM$.\\\\
                    Do $T \\in SM \\subset (SBD)$, nên $T$ là giao điểm của $IK$ và $(SBD)$.\\\\
                b) Tìm giao điểm của $\\text{mp}(IJK)$ với $SD$\\\\
                Tìm giao điểm $Q$ của $SD$ với $\\text{mp}(IJK)$\\\\
                    Trong $\\text{mp}(ABCD)$, gọi $P = KJ \\cap AD$. ($P$ là điểm chung của $(IJK)$ và $(SAD)$).\\\\
                Tìm giao tuyến $IP$ của $\\text{mp}(IJK)$ và $\\text{mp}(SAD)$.\\\\
                    Giao tuyến là đường thẳng $IP$ (vì $I \\in SA$ và $P$ là hai điểm chung).\\\\
                    Trong $\\text{mp}(SAD)$, gọi $Q = SD \\cap IP$.\\\\
                    Do $Q \\in IP \\subset (IJK)$, nên $Q$ là giao điểm của $SD$ và $(IJK)$.''')

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

