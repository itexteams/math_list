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


def bt_dang3_p4_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(2,9)


                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$, đáy $ABCD$ có $AB$ cắt $CD$ tại $E$, $AC$ cắt $BD$ tại $F$. \\\\
                                 a) Tìm giao tuyến của các cặp mặt phẳng $(SAB)$ và $(SCD)$, $(SAC)$ và $(SBD)$. \\\\
                                b) Tìm giao tuyến của $(SEF)$ với các mặt phẳng $(SAD), (SBD)$.'''
                                 %(
                                 ))

                # Nội dung lời giải
                loigiai = (    '''\\begin{center}
            	\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
            		\\clip(-1.444120042671654,-2.399382063795924) rectangle (4.519706605503896,3.5644445843796206);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (-1.,-2.);
            		\\draw [line width=1.pt ] (-1.,-2.)-- (0.,3.);
            		\\draw [line width=1.pt ] (0.,3.)-- (4.,0.);
            		\\draw [line width=1.pt ] (4.,0.)-- (-1.,-2.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (0.,3.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (-0.508,-1.016)-- (4.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (-1.,-2.)-- (2.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (1.4931034482758623,-1.002758620689655);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (2.,0.)-- (1.4931034482758623,-1.002758620689655);
            		\\draw [line width=1.pt ] (0.,3.)-- (1.4931034482758623,-1.002758620689655);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,3.)-- (0.9785522788203753,-0.6809651474530831);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,3.)-- (2.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,3.)-- (-0.508,-1.016);
            		\\draw (-0.3,3.4937272723459185) node[anchor=north west] {$S$};
            		\\draw (-0.1,0.45) node[anchor=north west] {$A$};
            		\\draw (1.9,0.5) node[anchor=north west] {$B$};
            		\\draw (1.4670759693824191,-0.890746073743612) node[anchor=north west] {$C$};
            		\\draw (-1.290899199931966,-2) node[anchor=north west] {$D$};
            		\\draw (4.048257858612549,0.3114482308293238) node[anchor=north west] {$E$};
            		\\draw (1.6,-0.37215245216312987) node[anchor=north west] {$H$};
            		\\draw (0.7,-0.5843043882642363) node[anchor=north west] {$F$};
            		\\draw (-0.5365812049058094,-0.9025322924158957) node[anchor=north west] {$G$};
            	\\end{tikzpicture}
            \\end{center}
            \\begin{enumEX}[a)]{1} \n
                                \\item  $\\heva{&E \\in AB \\Rightarrow SE \\subset (SAB) \\\\& E \\in AC \\Rightarrow SE \\subset (SCD)} \\Rightarrow (SAB) \\cap (SCD)=SE.$ \\\\
                                    $\\heva{&F \\in AC \\Rightarrow SF \\subset (SAC) \\\\& F \\in BD \\Rightarrow SF \\subset (SBD)} \\Rightarrow (SAC) \\cap (SBD)=SF.$ \\\\
                                \\item  Gọi $G$ là giao điểm của $EF$ và $AD$, $H$ là giao điểm của $EF$ và $BC$, ta có \\\\
                                    $\\heva{&G \\in EF \\Rightarrow SG \\subset (SEF) \\\\& G \\in AD \\Rightarrow SG \\subset (SAD)} \\Rightarrow (SEF) \\cap (SAD)=SG.$ \\\\
                                        $\\heva{&H \\in EF \\Rightarrow SH \\subset (SEF) \\\\& H \\in AD \\Rightarrow SH \\subset (SBC)} \\Rightarrow (SEF) \\cap (SBC)=SH.$ \\\\
                                \\end{enumEX}'''

                           %(
                           ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

