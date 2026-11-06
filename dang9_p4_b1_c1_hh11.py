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


def bt_dang9_p4_b1_c1_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':


                # Nội dung câu hỏi
                noidungcauhoi =  ('''Cho hình chóp $S.ABCD$. $M$ là một điểm trên cạnh $SC$.\\\\
            a) Tìm giao điểm của $AM$ và mặt phẳng $(SBD)$.\\\\
            b) Gọi $N$ là một điểm trên cạnh $BC$. Tìm giao điểm của $SD$ và mặt phẳng $(AMN)$.'''
                )

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                           \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,scale=0.6]
            	\\clip(-2.2636123183833723,-5.166977609074535) rectangle (9.98615614177243,7.211060677889189);
            	\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (8.,0.);
            	\\draw (8.,0.)-- (6.4958,-1.9274);
            	\\draw (0.9558,-2.2474)-- (0.,0.);
            	\\draw (4.,6.)-- (0.,0.);
            	\\draw (4.,6.)-- (0.9558,-2.2474);
            	\\draw (4.,6.)-- (8.,0.);
            	\\draw (4.,6.)-- (6.4958,-1.9274);
            	\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (6.4958,-1.9274);
            	\\draw [dash pattern=on 2pt off 2pt] (0.9558,-2.2474)-- (8.,0.);
            	\\draw [dash pattern=on 2pt off 2pt] (8.,0.)-- (5.094798122793035,-2.008324296156359);
            	\\draw (5.094798122793035,-2.008324296156359)-- (1.8176095806224424,-4.273797626585977);
            	\\draw (0.9558,-2.2474)-- (1.8176095806224424,-4.273797626585977);
            	\\draw [dash pattern=on 2pt off 2pt] (4.145042938491716,-1.229895587864302)-- (4.,6.);
            	\\draw [dash pattern=on 2pt off 2pt] (8.,0.)-- (2.7511320927411322,2.616545174979704);
            	\\draw (2.7511320927411322,2.616545174979704)-- (5.094798122793035,-2.008324296156359);
            	\\draw (2.7511320927411322,2.616545174979704)-- (1.8176095806224424,-4.273797626585977);
            	\\draw (2.7511320927411322,2.616545174979704)-- (3.0079165426325734,4.511874813948861);
            	\\draw [dash pattern=on 2pt off 2pt] (0.9558,-2.2474)-- (5.1152389074927145,-1.9941938755246837);
            	\\draw (5.1152389074927145,-1.9941938755246837)-- (6.4958,-1.9274);
            	\\draw (3.722312932652622,7.10416915554926) node[anchor=north west] {$S$};
            	\\draw (-0.88,0.7120561196215343) node[anchor=north west] {$D$};
            	\\draw (2.3541014467015375,5.3) node[anchor=north west] {$T$};
            	\\draw (4.107122413076365,2.8926431753560764) node[anchor=north west] {$J$};
            	\\draw (1.7,3.2560743513118333) node[anchor=north west] {$M$};
            	\\draw (3.722312932652622,-1.2) node[anchor=north west] {$O$};
            	\\draw (4.5,-2) node[anchor=north west] {$N$};
            	\\draw (8.318648393269546,0.7120561196215343) node[anchor=north west] {$A$};
            	\\draw (-0.2,-1.8533404165367504) node[anchor=north west] {$C$};
            	\\draw (0.7,-4) node[anchor=north west] {$K$};
            	\\draw (6.501492513490762,-1.6609356763248793) node[anchor=north west] {$B$};
            \\end{tikzpicture}
                           \\end{center}'''
                    '''a) Tìm giao điểm $J$ của $AM$ và $(SBD)$\\\\
                    Chọn $\\text{mp}(SAC)$ chứa đường thẳng $AM$.\\\\
                    Gọi $O = AC \\cap BD$ (Trong $\\text{mp}(ABCD)$).\\\\
                    Trong $\\text{mp}(SAC)$, gọi $J = AM \\cap SO$.\\\\
                    Do $J \\in SO \\subset (SBD)$, nên $J$ là giao điểm của $AM$ và $(SBD)$.\\\\
                b) Tìm giao điểm $T$ của $SD$ và $(AMN)$\\\\
                    Trong $\\text{mp}(ABCD)$ (mặt phẳng đáy), gọi $K = AN \\cap CD$.\\\\
                    Khi đó $K$ là điểm chung của $(AMN)$ và mặt phẳng $(SCD)$ (chứa $SD$).\\\\
                Tìm giao tuyến của $\\text{mp}(AMN)$ và $\\text{mp}(SCD)$.\\\\
                    Hai điểm chung là $M$ (vì $M \\in SC$) và $K$.\\\\
                    Giao tuyến là đường thẳng $MK$.\\\\
                    Trong $\\text{mp}(SCD)$, gọi $T = SD \\cap MK$.\\\\
                    Do $T \\in MK \\subset (AMN)$, nên $T$ là giao điểm của $SD$ và $(AMN)$.''')

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

