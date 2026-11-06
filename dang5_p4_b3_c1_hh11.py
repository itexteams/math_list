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


def bt_dang5_p4_b3_c1_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                #Khai báo biến
                a=randint(2,9)
                #Các đáp án trắc nghiệm
                du = ['''$MN // (ABCD)$''',
                      ]
                da= random.choice(du)
                s = ['''$MN // (SCD)$''',
                     '''$NP // (SAD)$''',
                     '''$MP // (SBC)$''',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành có tâm $O$. Gọi $N$ là trung điểm của cạnh $AB$. Gọi $G$ là trọng tâm của tam giác $SAN$. Chứng minh $OG // (SBC)$.'''
                                 %(
                                 ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''\\begin{center}
            	\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
            		\\clip(-0.6161039091545139,-0.48267871063312084) rectangle (5.471349314200825,4.663986287294566);
            		\\draw [line width=1.pt] (0.,0.)-- (4.,0.);
            		\\draw [line width=1.pt] (4.,0.)-- (5.,1.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (1.,1.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (5.,1.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,4.)-- (1.,1.);
            		\\draw [line width=1.pt] (2.,4.)-- (0.,0.);
            		\\draw [line width=1.pt] (2.,4.)-- (4.,0.);
            		\\draw [line width=1.pt] (2.,4.)-- (5.,1.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (4.,0.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,1.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,1.)-- (2.,4.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,1.)-- (2.5,0.5);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.5,0.5)-- (1.5055425921808103,2.516627776542431);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.5055425921808103,2.516627776542431)-- (3.,1.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,4.)-- (2.,1.);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (2.5072650611757963,2.478204816472611);
            		\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.017095584361441,1.9974858638621045)-- (2.5,0.5);
            		\\draw (1.8327125011497931,4.6778214082567375) node[anchor=north west] {$S$};
            		\\draw (0.5,1.5095787079195322) node[anchor=north west] {$A$};
            		\\draw (4.987120080524833,1.3850626192599913) node[anchor=north west] {$B$};
            		\\draw (3.9356508873998193,0.22291245843761046) node[anchor=north west] {$C$};
            		\\draw (-0.6,0.23674757939978167) node[anchor=north west] {$D$};
            		\\draw (2.24776613001493,0.5) node[anchor=north west] {$O$};
            		\\draw (1.514504719019855,3.017606892796193) node[anchor=north west] {$M$};
            		\\draw (2.7,1.5787543127303882) node[anchor=north west] {$N$};
            		\\draw (2.0955797994310466,2.4088615704606604) node[anchor=north west] {$G$};
            	\\end{tikzpicture}
            \\end{center}
            Gọi $M$ là trung điểm của $SA$. \\\\
                         Xét tam giác $ABC$ có $ON$ là đường trung bình ứng với cạnh $BC$. \\\\
                             Suy ra $ON // BC$ nên $ON // (SBC)$. \\\\
                                 Xét tam giác $SAC$ có $OM$ là đường trung bình ứng với cạnh $SC$.\\\\
                                     Suy ra $OM // SC$ nên $OM // (SBC)$. \\\\
                                         Vì $G$ là trọng tâm của tam giác $SAN$ nên $G \\in (OMN)$ mà $(OMN) // (SBC)$ nên $OG // (SBC)$.'''
                         %(
                         ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-')
            return content

