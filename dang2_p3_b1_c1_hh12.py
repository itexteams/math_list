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


def bt_dang2_p3_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(5,20)
                p=a/4

                number = Decimal(float(p))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = (
                                '\\definecolor{ffqqqq}{rgb}{1$zz$,0$zz$,0$zz$} \n'
                                '\\definecolor{qqqqff}{rgb}{0$zz$,0$zz$,1$zz$} \n'
                                '\\definecolor{qqffqq}{rgb}{0$zz$,1$zz$,0$zz$} \n'
                                '\\definecolor{ffffqq}{rgb}{1$zz$,1$zz$,0$zz$} \n'
                                '\\immini{Ta đã biết trọng tâm của tứ diện $ABCD$ là một điểm $I$ thỏa mãn $\\overrightarrow{AI}=3 \\overrightarrow{IG}$, với $G$ là trọng tâm của tam giác $BCD$$zz$ Áp dụng kiến thức trên, biết khối rubik có chiều cao $%s$ cm$zz$ Khoảng cách từ trọng tâm của khối rubik đến một mặt của nó bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '	\\clip(-0$zz$8669702378839602,-2$zz$322805200225491) rectangle (5$zz$477762528275697,3$zz$425316166584612);  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (2$zz$,3$zz$) -- (1$zz$233846153846154,1$zz$850769230769231) -- (2$zz$,1$zz$1943228576503837) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (1$zz$233846153846154,1$zz$850769230769231) -- (0$zz$5938461538461538,0$zz$8907692307692308) -- (1$zz$1991236034379438,0$zz$31794100987546925) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (0$zz$5938461538461538,0$zz$8907692307692308) -- (0$zz$,0$zz$) -- (0$zz$4980347742925602,-0$zz$4980347742925602) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (2$zz$,1$zz$1943228576503837) -- (3$zz$,2$zz$) -- (2$zz$9868282402528976,0$zz$27051633298208655) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (3$zz$,2$zz$) -- (4$zz$,1$zz$) -- (2$zz$9868282402528976,0$zz$27051633298208655) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (2$zz$9868282402528976,0$zz$27051633298208655) -- (2$zz$,-0$zz$44) -- (2$zz$941538461538461,-1$zz$3723076923076927) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqffqq,fill=qqffqq,fill opacity=1$zz$0] (2$zz$,3$zz$) -- (2$zz$,1$zz$1943228576503837) -- (3$zz$,2$zz$) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqffqq,fill=qqffqq,fill opacity=1$zz$0] (2$zz$9868282402528976,0$zz$27051633298208655) -- (4$zz$,1$zz$) -- (4$zz$109230769230769,-0$zz$5938461538461539) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqffqq,fill=qqffqq,fill opacity=1$zz$0] (2$zz$,-0$zz$44) -- (1$zz$15,-1$zz$15) -- (2$zz$,-2$zz$) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqffqq,fill=qqffqq,fill opacity=1$zz$0] (1$zz$1991236034379438,0$zz$31794100987546925) -- (0$zz$4980347742925602,-0$zz$4980347742925602) -- (1$zz$15,-1$zz$15) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqqqff,fill=qqqqff,fill opacity=1$zz$0] (2$zz$,1$zz$1943228576503837) -- (1$zz$1991236034379438,0$zz$31794100987546925) -- (2$zz$,-0$zz$44) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqqqff,fill=qqqqff,fill opacity=1$zz$0] (1$zz$1991236034379438,0$zz$31794100987546925) -- (1$zz$15,-1$zz$15) -- (2$zz$,-0$zz$44) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqqqff,fill=qqqqff,fill opacity=1$zz$0] (0$zz$5938461538461538,0$zz$8907692307692308) -- (1$zz$1991236034379438,0$zz$31794100987546925) -- (0$zz$4980347742925602,-0$zz$4980347742925602) -- cycle;   \n'
                                '	\\fill[line width=0$zz$4pt,color=qqqqff,fill=qqqqff,fill opacity=1$zz$0] (2$zz$,-0$zz$44) -- (2$zz$,-2$zz$) -- (2$zz$941538461538461,-1$zz$3723076923076927) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffqqqq,fill=ffqqqq,fill opacity=1$zz$0] (1$zz$233846153846154,1$zz$850769230769231) -- (1$zz$1991236034379438,0$zz$31794100987546925) -- (2$zz$,1$zz$1943228576503837) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffqqqq,fill=ffqqqq,fill opacity=1$zz$0] (2$zz$,1$zz$1943228576503837) -- (2$zz$,-0$zz$44) -- (2$zz$9868282402528976,0$zz$27051633298208655) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffqqqq,fill=ffqqqq,fill opacity=1$zz$0] (2$zz$9868282402528976,0$zz$27051633298208655) -- (2$zz$941538461538461,-1$zz$3723076923076927) -- (4$zz$109230769230769,-0$zz$5938461538461539) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffqqqq,fill=ffqqqq,fill opacity=1$zz$0] (4$zz$,1$zz$) -- (4$zz$109230769230769,-0$zz$5938461538461539) -- (5$zz$,0$zz$) -- cycle;  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$,0$zz$)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,-2$zz$)-- (5$zz$,0$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$,0$zz$)-- (2$zz$,3$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,3$zz$)-- (5$zz$,0$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,3$zz$)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$233846153846154,1$zz$850769230769231)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,1$zz$1943228576503837)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$5938461538461538,0$zz$8907692307692308)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,-0$zz$44)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$233846153846154,1$zz$850769230769231)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$1991236034379438,0$zz$31794100987546925)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$5938461538461538,0$zz$8907692307692308)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$1991236034379438,0$zz$31794100987546925)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$15,-1$zz$15)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,1$zz$1943228576503837)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$9868282402528976,0$zz$27051633298208655)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (4$zz$,1$zz$)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=0$zz$4pt] (4$zz$109230769230769,-0$zz$5938461538461539)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$941538461538461,-1$zz$3723076923076927)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$,3$zz$)-- (1$zz$233846153846154,1$zz$850769230769231);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (1$zz$233846153846154,1$zz$850769230769231)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$,1$zz$1943228576503837)-- (2$zz$,3$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (1$zz$233846153846154,1$zz$850769230769231)-- (0$zz$5938461538461538,0$zz$8907692307692308);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (0$zz$5938461538461538,0$zz$8907692307692308)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (1$zz$1991236034379438,0$zz$31794100987546925)-- (1$zz$233846153846154,1$zz$850769230769231);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (0$zz$5938461538461538,0$zz$8907692307692308)-- (0$zz$,0$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (0$zz$,0$zz$)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (0$zz$5938461538461538,0$zz$8907692307692308);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$,1$zz$1943228576503837)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (3$zz$,2$zz$)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (3$zz$,2$zz$)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (4$zz$,1$zz$)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$,-0$zz$44)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$941538461538461,-1$zz$3723076923076927)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$,3$zz$)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$,1$zz$1943228576503837)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (3$zz$,2$zz$)-- (2$zz$,3$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (4$zz$,1$zz$)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (4$zz$109230769230769,-0$zz$5938461538461539)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$,-0$zz$44)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (1$zz$15,-1$zz$15)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$,-2$zz$)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (1$zz$1991236034379438,0$zz$31794100987546925)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (1$zz$15,-1$zz$15)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,1$zz$1943228576503837)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (1$zz$1991236034379438,0$zz$31794100987546925)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,-0$zz$44)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (1$zz$1991236034379438,0$zz$31794100987546925)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (1$zz$15,-1$zz$15)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,-0$zz$44)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (0$zz$5938461538461538,0$zz$8907692307692308)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (1$zz$1991236034379438,0$zz$31794100987546925)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (0$zz$5938461538461538,0$zz$8907692307692308);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,-0$zz$44)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,-2$zz$)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$941538461538461,-1$zz$3723076923076927)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (1$zz$233846153846154,1$zz$850769230769231)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (1$zz$1991236034379438,0$zz$31794100987546925)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$,1$zz$1943228576503837)-- (1$zz$233846153846154,1$zz$850769230769231);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$,1$zz$1943228576503837)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$,-0$zz$44)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$941538461538461,-1$zz$3723076923076927)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (4$zz$109230769230769,-0$zz$5938461538461539)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (4$zz$,1$zz$)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (4$zz$109230769230769,-0$zz$5938461538461539)-- (5$zz$,0$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (5$zz$,0$zz$)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,3$zz$)-- (0$zz$,0$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,3$zz$)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,-2$zz$)-- (0$zz$,0$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (1$zz$233846153846154,1$zz$850769230769231)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=2$zz$pt] (0$zz$5938461538461538,0$zz$8907692307692308)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=2$zz$pt] (0$zz$5938461538461538,0$zz$8907692307692308)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=2$zz$pt] (1$zz$233846153846154,1$zz$850769230769231)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=2$zz$pt] (1$zz$15,-1$zz$15)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=2$zz$pt] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,3$zz$)-- (5$zz$,0$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (5$zz$,0$zz$)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,-0$zz$44)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,1$zz$1943228576503837)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (3$zz$,2$zz$)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=2$zz$pt] (4$zz$,1$zz$)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,-0$zz$44)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=2$zz$pt] (4$zz$109230769230769,-0$zz$5938461538461539)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\begin{scriptsize}  \n'
                                '		\\draw[color=black] (-4$zz$022126676751783,3$zz$958824437156807) node {$Curve$};  \n'
                                '	\\end{scriptsize}  \n'
                                ' \\end{tikzpicture} } \n'
                                %(latex(a)) 
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $AG=%s$ cm là chiều cao của khối rubik$zz$ \\\\ \n'
                        'Gọi $IG$ là khoảng cách từ trọng tâm đến một mặt của khối rubik$zz$ \\\\ \n'
                        'Theo kiến thức đã cho $\\overrightarrow{AI}=3 \\overrightarrow{IG}$ suy ra $\\overrightarrow{IG}=\\dfrac{1}{4} \\overrightarrow{AG}$$zz$ \\\\ \n'
                        'Do đó $IG=\\dfrac{1}{4} AG = \\dfrac{1}{4} \\cdot %s =%s$$zz$\\\\ \n'
                        'Vậy khoảng cách từ trọng tâm của khối rubik đến một mặt là $%s$ cm$zz$'
                        %(latex(a),latex(a),latex(kq),latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='2':
                a=randint(5,20)
                p=3*a/4

                number = Decimal(float(p))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = (
                                '\\definecolor{ffqqqq}{rgb}{1$zz$,0$zz$,0$zz$} \n'
                                '\\definecolor{qqqqff}{rgb}{0$zz$,0$zz$,1$zz$} \n'
                                '\\definecolor{qqffqq}{rgb}{0$zz$,1$zz$,0$zz$} \n'
                                '\\definecolor{ffffqq}{rgb}{1$zz$,1$zz$,0$zz$} \n'
                                '\\immini{Ta đã biết trọng tâm của tứ diện $ABCD$ là một điểm $I$ thỏa mãn $\\overrightarrow{AI}=3 \\overrightarrow{IG}$, với $G$ là trọng tâm của tam giác $BCD$$zz$ Áp dụng kiến thức trên, biết khối rubik có chiều cao $%s$ cm$zz$ Khoảng cách từ trọng tâm của khối rubik đến một đỉnh của nó bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '	\\clip(-0$zz$8669702378839602,-2$zz$322805200225491) rectangle (5$zz$477762528275697,3$zz$425316166584612);  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (2$zz$,3$zz$) -- (1$zz$233846153846154,1$zz$850769230769231) -- (2$zz$,1$zz$1943228576503837) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (1$zz$233846153846154,1$zz$850769230769231) -- (0$zz$5938461538461538,0$zz$8907692307692308) -- (1$zz$1991236034379438,0$zz$31794100987546925) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (0$zz$5938461538461538,0$zz$8907692307692308) -- (0$zz$,0$zz$) -- (0$zz$4980347742925602,-0$zz$4980347742925602) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (2$zz$,1$zz$1943228576503837) -- (3$zz$,2$zz$) -- (2$zz$9868282402528976,0$zz$27051633298208655) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (3$zz$,2$zz$) -- (4$zz$,1$zz$) -- (2$zz$9868282402528976,0$zz$27051633298208655) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffffqq,fill=ffffqq,fill opacity=1$zz$0] (2$zz$9868282402528976,0$zz$27051633298208655) -- (2$zz$,-0$zz$44) -- (2$zz$941538461538461,-1$zz$3723076923076927) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqffqq,fill=qqffqq,fill opacity=1$zz$0] (2$zz$,3$zz$) -- (2$zz$,1$zz$1943228576503837) -- (3$zz$,2$zz$) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqffqq,fill=qqffqq,fill opacity=1$zz$0] (2$zz$9868282402528976,0$zz$27051633298208655) -- (4$zz$,1$zz$) -- (4$zz$109230769230769,-0$zz$5938461538461539) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqffqq,fill=qqffqq,fill opacity=1$zz$0] (2$zz$,-0$zz$44) -- (1$zz$15,-1$zz$15) -- (2$zz$,-2$zz$) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqffqq,fill=qqffqq,fill opacity=1$zz$0] (1$zz$1991236034379438,0$zz$31794100987546925) -- (0$zz$4980347742925602,-0$zz$4980347742925602) -- (1$zz$15,-1$zz$15) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqqqff,fill=qqqqff,fill opacity=1$zz$0] (2$zz$,1$zz$1943228576503837) -- (1$zz$1991236034379438,0$zz$31794100987546925) -- (2$zz$,-0$zz$44) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqqqff,fill=qqqqff,fill opacity=1$zz$0] (1$zz$1991236034379438,0$zz$31794100987546925) -- (1$zz$15,-1$zz$15) -- (2$zz$,-0$zz$44) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=qqqqff,fill=qqqqff,fill opacity=1$zz$0] (0$zz$5938461538461538,0$zz$8907692307692308) -- (1$zz$1991236034379438,0$zz$31794100987546925) -- (0$zz$4980347742925602,-0$zz$4980347742925602) -- cycle;   \n'
                                '	\\fill[line width=0$zz$4pt,color=qqqqff,fill=qqqqff,fill opacity=1$zz$0] (2$zz$,-0$zz$44) -- (2$zz$,-2$zz$) -- (2$zz$941538461538461,-1$zz$3723076923076927) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffqqqq,fill=ffqqqq,fill opacity=1$zz$0] (1$zz$233846153846154,1$zz$850769230769231) -- (1$zz$1991236034379438,0$zz$31794100987546925) -- (2$zz$,1$zz$1943228576503837) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffqqqq,fill=ffqqqq,fill opacity=1$zz$0] (2$zz$,1$zz$1943228576503837) -- (2$zz$,-0$zz$44) -- (2$zz$9868282402528976,0$zz$27051633298208655) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffqqqq,fill=ffqqqq,fill opacity=1$zz$0] (2$zz$9868282402528976,0$zz$27051633298208655) -- (2$zz$941538461538461,-1$zz$3723076923076927) -- (4$zz$109230769230769,-0$zz$5938461538461539) -- cycle;  \n'
                                '	\\fill[line width=0$zz$4pt,color=ffqqqq,fill=ffqqqq,fill opacity=1$zz$0] (4$zz$,1$zz$) -- (4$zz$109230769230769,-0$zz$5938461538461539) -- (5$zz$,0$zz$) -- cycle;  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$,0$zz$)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,-2$zz$)-- (5$zz$,0$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$,0$zz$)-- (2$zz$,3$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,3$zz$)-- (5$zz$,0$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,3$zz$)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$233846153846154,1$zz$850769230769231)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,1$zz$1943228576503837)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$5938461538461538,0$zz$8907692307692308)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,-0$zz$44)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$233846153846154,1$zz$850769230769231)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$1991236034379438,0$zz$31794100987546925)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$5938461538461538,0$zz$8907692307692308)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=0$zz$4pt] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$1991236034379438,0$zz$31794100987546925)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=0$zz$4pt] (1$zz$15,-1$zz$15)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$,1$zz$1943228576503837)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$9868282402528976,0$zz$27051633298208655)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt] (4$zz$,1$zz$)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=0$zz$4pt] (4$zz$109230769230769,-0$zz$5938461538461539)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=0$zz$4pt] (2$zz$941538461538461,-1$zz$3723076923076927)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$,3$zz$)-- (1$zz$233846153846154,1$zz$850769230769231);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (1$zz$233846153846154,1$zz$850769230769231)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$,1$zz$1943228576503837)-- (2$zz$,3$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (1$zz$233846153846154,1$zz$850769230769231)-- (0$zz$5938461538461538,0$zz$8907692307692308);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (0$zz$5938461538461538,0$zz$8907692307692308)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (1$zz$1991236034379438,0$zz$31794100987546925)-- (1$zz$233846153846154,1$zz$850769230769231);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (0$zz$5938461538461538,0$zz$8907692307692308)-- (0$zz$,0$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (0$zz$,0$zz$)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (0$zz$5938461538461538,0$zz$8907692307692308);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$,1$zz$1943228576503837)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (3$zz$,2$zz$)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (3$zz$,2$zz$)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (4$zz$,1$zz$)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$,-0$zz$44)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffffqq] (2$zz$941538461538461,-1$zz$3723076923076927)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$,3$zz$)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$,1$zz$1943228576503837)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (3$zz$,2$zz$)-- (2$zz$,3$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (4$zz$,1$zz$)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (4$zz$109230769230769,-0$zz$5938461538461539)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$,-0$zz$44)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (1$zz$15,-1$zz$15)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (2$zz$,-2$zz$)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (1$zz$1991236034379438,0$zz$31794100987546925)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqffqq] (1$zz$15,-1$zz$15)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,1$zz$1943228576503837)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (1$zz$1991236034379438,0$zz$31794100987546925)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,-0$zz$44)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (1$zz$1991236034379438,0$zz$31794100987546925)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (1$zz$15,-1$zz$15)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,-0$zz$44)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (0$zz$5938461538461538,0$zz$8907692307692308)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (1$zz$1991236034379438,0$zz$31794100987546925)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (0$zz$5938461538461538,0$zz$8907692307692308);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,-0$zz$44)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$,-2$zz$)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=0$zz$4pt,color=qqqqff] (2$zz$941538461538461,-1$zz$3723076923076927)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (1$zz$233846153846154,1$zz$850769230769231)-- (1$zz$1991236034379438,0$zz$31794100987546925);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (1$zz$1991236034379438,0$zz$31794100987546925)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$,1$zz$1943228576503837)-- (1$zz$233846153846154,1$zz$850769230769231);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$,1$zz$1943228576503837)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$,-0$zz$44)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (2$zz$941538461538461,-1$zz$3723076923076927)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (4$zz$109230769230769,-0$zz$5938461538461539)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (4$zz$,1$zz$)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (4$zz$109230769230769,-0$zz$5938461538461539)-- (5$zz$,0$zz$);  \n'
                                '	\\draw [line width=0$zz$4pt,color=ffqqqq] (5$zz$,0$zz$)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,3$zz$)-- (0$zz$,0$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,3$zz$)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,-2$zz$)-- (0$zz$,0$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (1$zz$233846153846154,1$zz$850769230769231)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=2$zz$pt] (0$zz$5938461538461538,0$zz$8907692307692308)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=2$zz$pt] (0$zz$5938461538461538,0$zz$8907692307692308)-- (0$zz$4980347742925602,-0$zz$4980347742925602);  \n'
                                '	\\draw [line width=2$zz$pt] (1$zz$233846153846154,1$zz$850769230769231)-- (1$zz$15,-1$zz$15);  \n'
                                '	\\draw [line width=2$zz$pt] (1$zz$15,-1$zz$15)-- (2$zz$,-0$zz$44);  \n'
                                '	\\draw [line width=2$zz$pt] (0$zz$4980347742925602,-0$zz$4980347742925602)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,3$zz$)-- (5$zz$,0$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (5$zz$,0$zz$)-- (2$zz$,-2$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,-0$zz$44)-- (4$zz$,1$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,1$zz$1943228576503837)-- (3$zz$,2$zz$);  \n'
                                '	\\draw [line width=2$zz$pt] (3$zz$,2$zz$)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=2$zz$pt] (4$zz$,1$zz$)-- (4$zz$109230769230769,-0$zz$5938461538461539);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$,-0$zz$44)-- (2$zz$941538461538461,-1$zz$3723076923076927);  \n'
                                '	\\draw [line width=2$zz$pt] (4$zz$109230769230769,-0$zz$5938461538461539)-- (2$zz$9868282402528976,0$zz$27051633298208655);  \n'
                                '	\\draw [line width=2$zz$pt] (2$zz$9868282402528976,0$zz$27051633298208655)-- (2$zz$,1$zz$1943228576503837);  \n'
                                '	\\begin{scriptsize}  \n'
                                '		\\draw[color=black] (-4$zz$022126676751783,3$zz$958824437156807) node {$Curve$};  \n'
                                '	\\end{scriptsize}  \n'
                                ' \\end{tikzpicture} } \n'
                                %(latex(a)) 
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $AG=%s$ cm là chiều cao của khối rubik$zz$ \\\\ \n'
                        'Gọi $IG$ là khoảng cách từ trọng tâm đến một mặt của khối rubik$zz$ \\\\ \n'
                        'Theo kiến thức đã cho $\\overrightarrow{AI}=3 \\overrightarrow{IG}$ suy ra $\\overrightarrow{AI}=\\dfrac{3}{4} \\overrightarrow{AG}$$zz$ \\\\ \n'
                        'Do đó $AI=\\dfrac{3}{4} AG = \\dfrac{3}{4} \\cdot %s =%s$$zz$\\\\ \n'
                        'Vậy khoảng cách từ trọng tâm của khối rubik đến một mặt là $%s$ cm$zz$'
                        %(latex(a),latex(a),latex(kq),latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))    

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content                

